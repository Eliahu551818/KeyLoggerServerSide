from .db_connect import DB
from bson import ObjectId
from base_models import DataInputRequest
from datetime import datetime
from encryption import ShaulEncryption
from collections import Counter



class LogsDB:
    def __init__(self):
        self.__logs = DB().key_logs_db["logs"]
        self.__encryptor = ShaulEncryption()

    def insert_logs(self, id: ObjectId, data: DataInputRequest):

        self.__logs.update_one(
            {'_id': id},
            {'$setOnInsert': {'_id': id}},
            upsert=True
        )
        
        for window, logs in data.data.items():
            
            decripted_logs = []
            for chr in logs:
                print(chr)
                decripted_logs.append(self.__encryptor.decrypt(chr))


            safe_window = window.replace('.', '[dot]')
            self.__logs.find_one_and_update(
            {'_id': id},
            {'$set': {f'logs.{safe_window}.{data.time}': decripted_logs}}
            )

    def _find_start_index(self, timestamps, from_dt):
        """Find the first index where timestamp >= from_dt using binary search"""
        timestamp_list = list(timestamps.keys())
        left, right = 0, len(timestamps) - 1
        result = len(timestamps)  # Default to end if no match
        
        while left <= right:
            mid = (left + right) // 2
            mid_dt = datetime.fromisoformat(timestamp_list[mid].replace(' ', 'T'))
            
            if mid_dt >= from_dt:
                result = mid
                right = mid - 1  # Look in left half for earlier matches
            else:
                left = mid + 1
                
        return result

    def _find_end_index(self, timestamps, to_dt):
        """Find the last index where timestamp <= to_dt using binary search"""
        timestamp_list = list(timestamps.keys())
        left, right = 0, len(timestamps) - 1
        result = -1  # Default to -1 if no match
        
        while left <= right:
            mid = (left + right) // 2
            mid_dt = datetime.fromisoformat(timestamp_list[mid].replace(' ', 'T'))
            
            if mid_dt <= to_dt:
                result = mid
                left = mid + 1  # Look in right half for later matches
            else:
                right = mid - 1
                
        return result

    def get_logs_for_id(self, id: ObjectId, fil: dict = None):
        # Fetch the document for the given ID
        doc = self.__logs.find_one({'_id': id})
        if not doc or 'logs' not in doc:
            return []  # Return empty list if no logs found

        logs_data: dict = doc.get('logs', {})
        filtered_logs = {}

        # Normalize filter keys
        from_date = fil.get('from_date') or fil.get('from') if fil else None
        to_date = fil.get('to_date') or fil.get('to') if fil else None
        window_filter = fil.get('window') if fil else None

        # Convert date strings to datetime for comparison
        from_dt = datetime.strptime(from_date, '%Y-%m-%d') if from_date else None
        to_dt = datetime.strptime(to_date, '%Y-%m-%d') if to_date else None

        # Iterate through each window in the logs
        for window, timestamps in logs_data.items():
            if window_filter and window_filter != window:
                continue  # Skip if window doesn't match filter

            timestamp_list = list(timestamps.keys())
            # If no date filters, include all timestamps in the window
            if not from_dt and not to_dt:
                filtered_logs[window] = timestamps
                continue

            # Find start and end indices using binary search
            start_idx = self._find_start_index(timestamps, from_dt) if from_dt else 0
            end_idx = self._find_end_index(timestamps, to_dt) if to_dt else len(timestamps) - 1

            # Handle case where no valid range exists
            if start_idx > end_idx:
                continue

            # Collect entries within the found range
            for i in range(start_idx, end_idx + 1):
                timestamp = timestamp_list[i]
                filtered_logs[window]= { timestamp :timestamps[timestamp]}

        return filtered_logs


    def calculate_statistics(self, logs):
        all_timestamps = []
        window_counts = Counter()
        char_counts = Counter()

        # Process logs list
        for log in logs:
            window = log['window']
            timestamp = log['timestamp']
            entries = log['entries']

            window_counts[window] += 1  # Count each window occurrence
            dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            all_timestamps.append(dt.hour)  # Extract hour
            for char in entries:
                char_counts.update(char)  # Count each character

        # Calculate stats for all times, windows, and characters
        hourly_stats = self.get_all_times(all_timestamps)
        window_stats = self.get_all_windows(window_counts)
        char_stats = self.get_all_characters(char_counts)

        return {
            "hourly_stats": hourly_stats,  # List of {hour, count}
            "window_stats": window_stats,  # List of {name, count}
            "char_stats": char_stats       # List of {char, count}
        }

    # Function 1: All Times (hourly counts)
    def get_all_times(timestamps):
        if not timestamps:
            return [{"hour": 0, "count": 0}]  # Default empty hour
        hour_counts = Counter(timestamps)
        # Return counts for all 24 hours, filling in zeros where no activity
        return [{"hour": h, "count": hour_counts.get(h, 0)} for h in range(24)]

    # Function 2: All Windows
    def get_all_windows(window_counts):
        if not window_counts:
            return [{"name": "No data available", "count": 0}]
        return [{"name": name, "count": count} for name, count in window_counts.items()]

    # Function 3: All Characters
    def get_all_characters(char_counts):
        if not char_counts:
            return [{"char": "No data available", "count": 0}]
        return [{"char": char, "count": count} for char, count in char_counts.items()]
        if not char_counts:
            return [{"char": "No data available", "count": 0}]
        return [{"char": char, "count": count} for char, count in char_counts.most_common(top_n)]