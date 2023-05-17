token = localStorage.getItem('accessToken')
owners = document.getElementById('owners')

const getOwners = async () => {
  var myHeaders = new Headers()
  myHeaders.append('Authorization', `Bearer ${token}`)

  var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow',
  }

  const response = await fetch(
    'http://127.0.0.1:3000/api/owners',
    requestOptions,
  )

  if (response.status === 200) {
    result = await response.json()
    console.log(result)
    owners.innerHTML = ''
    for (owner of result) {
      // <li class="list-group-item">An item</li>
      el = document.createElement('li')
      el.className = 'list-group-item'
      el.innerHTML = `ID: ${owner.id} email: ${owner.email}`

      owners.appendChild(el)
    }
  }
}

getOwners()
