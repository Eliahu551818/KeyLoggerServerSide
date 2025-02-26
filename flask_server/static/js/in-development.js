document.addEventListener('DOMContentLoaded', () => {
    const progress = document.getElementById('progress');
    
    // Simulate development progress
    let progressWidth = 0;
    const maxProgress = 70; // Set to 70% to show it's still in progress

    function updateProgress() {
        if (progressWidth < maxProgress) {
            progressWidth += 1;
            progress.style.width = `${progressWidth}%`;
            setTimeout(updateProgress, 50);
        }
    }

    // Start the progress animation
    updateProgress();
});