const employeeTable = document.getElementById("employeeTable");
const employeeTableBody = document.getElementById("employeeBody");
const reimbursementTable = document.getElementById("reimbursementTable");
const reimbursementTableBody = document.getElementById("reimbursementBody");
const email = sessionStorage.getItem("email");

async function getAllEmployeeData(){
    let url = "http://127.0.0.1:5000/employee/" + email.toLowerCase();
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateEmployeeData(body);
        getAllReimbursementData();
    }   else{
        alert("There was a problem trying to get the employee information: sorry!");
    }
}

async function getAllReimbursementData(){
    let employeeID = sessionStorage.getItem("employeeID")
    let url = "http://127.0.0.1:5000/employee/" + employeeID + "/reimbursements";
    let response = await fetch(url);
    if (response.status === 200){
        let body = await response.json();
        populateReimbursementData(body);
    }   else{
        alert("There was a problem trying to get the reimbursement information: sorry!");
    }
}

function populateEmployeeData(employee){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${employee.employeeID}</td><td>${employee.firstName}</td><td>${employee.lastName}</td><td>${employee.email}</td>`;
        employeeTableBody.appendChild(tableRow);
        sessionStorage.setItem("employeeID", employee.employeeID);
}

function populateReimbursementData(responseBody){
    for(let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementID}</td><td>${reimbursement.managerID}</td><td>${reimbursement.amount}</td><td>${reimbursement.approval}</td><td>${reimbursement.message}</td><td>${reimbursement.managerComment}</td>`;
        reimbursementTableBody.appendChild(tableRow);
    }
}

function logout(){
    sessionStorage.clear();
    window.location.href="../html/login_page.html";
}
getAllEmployeeData();
