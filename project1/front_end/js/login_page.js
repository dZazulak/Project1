async function getManagerEmailAndPassword(){
    let url = "http://127.0.0.1:5000/manager/managerLogin";
    const email = document.getElementById("email");
    const passcode = document.getElementById("passcode");

    sessionStorage.setItem("email", email.value);
    sessionStorage.setItem("passcode", passcode.value);
    console.log(email.value);
    console.log(passcode.value);
    managerJSON = JSON.stringify({"email": email.value.toLowerCase(), "passcode": passcode.value});
    console.log(managerJSON);

    let response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": 'application/json'},
        body:managerJSON}).then(response => {return response.json()});

    if (response.email == email.value.toLowerCase() && response.passcode == passcode.value){
        window.location.href = "../html/manager_page.html";
    }   else{
        alert("Invalid username or password");
    }
}

async function getEmployeeEmailAndPassword(){
    let url = "http://127.0.0.1:5000/employee/employeeLogin"
    const email = document.getElementById("email");
    const passcode = document.getElementById("passcode");

    sessionStorage.setItem("email", email.value);
    sessionStorage.setItem("passcode", passcode.value);
    console.log(email.value);
    console.log(passcode.value);
    employeeJSON = JSON.stringify({"email": email.value.toLowerCase(), "passcode": passcode.value});
    console.log(employeeJSON);

    let response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": 'application/json'},
        body:employeeJSON}).then(response => {return response.json()});

    if (response.email == email.value.toLowerCase() && response.passcode == passcode.value){
        window.location.href = "../html/employee_page.html";
    }   else{
        getManagerEmailAndPassword();
    }
}