const managerTable = document.getElementById("managerTable");
const managerTableBody = document.getElementById("managerBody");
const pendingReimbursementTable = document.getElementById("pendingReimbursementTable");
const pendingReimbursementTableBody = document.getElementById("pendingReimbursementBody");
const pastReimbursementTable = document.getElementById("pastReimbursementTable");
const pastReimbursementTableBody = document.getElementById("pastReimbursementBody");
const statisticsTable = document.getElementById("statisticsTable");
const statisticsBody = document.getElementById("statisticsBody");
const email = sessionStorage.getItem("email");



async function getAllManagerData(){
    let url = "http://127.0.0.1:5000/manager/" + email.toLowerCase();
    let response = await fetch(url);

    if(response.status === 200){
        let body = await response.json();
        console.log(body);
        populateManagerData(body);
        getAllPendingReimbursementData();
        getAllPastReimbursementData();
    }   else{
        alert("There was a problem trying to get the manager information: sorry!");
    }
}

async function getAllPendingReimbursementData(){
    let managerID = sessionStorage.getItem("managerID")
    let url = "http://127.0.0.1:5000/manager/" + managerID + "/pending_reimbursements";
    let response = await fetch(url);
    if (response.status === 200){
        let body = await response.json();
        populatePendingReimbursementData(body);
    }   else{
        alert("There was a problem trying to get the pending reimbursement information: sorry!");
    }
}

async function getAllPastReimbursementData(){
    let managerID = sessionStorage.getItem("managerID")
    let url = "http://127.0.0.1:5000/manager/" + managerID + "/past_reimbursements";
    let response = await fetch(url);
    if (response.status === 200){
        let body = await response.json();
        populatePastReimbursementData(body);
    }   else{
        alert("There was a problem trying to get the past reimbursement information: sorry!");
    }
}



function populateManagerData(manager){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${manager.managerID}</td><td>${manager.firstName}</td><td>${manager.lastName}</td><td>${manager.email}</td>`;
        managerTableBody.appendChild(tableRow);
        sessionStorage.setItem("managerID", manager.managerID);
}

function populatePendingReimbursementData(responseBody){
    let arr = []
    let index = 0;
    for(let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementID}</td><td>${reimbursement.employeeID}</td><td>${reimbursement.amount}</td><td>${reimbursement.approval}</td><td>${reimbursement.message}</td><td><input type="text" placeholder="Comment" id="managerComment${reimbursement.reimbursementID}"></td><td><button onclick="updateApprovedReimbursement(${reimbursement.reimbursementID})" id="approve${reimbursement.reimbursementID}">Approve</button><button onclick="updateDeniedReimbursement(${reimbursement.reimbursementID})" id="deny${reimbursement.reimbursementID}">Deny</button>`;
        
        pendingReimbursementTableBody.appendChild(tableRow);

        let pendingReimbursementJSON = JSON.stringify({"reimbursementId": reimbursement.reimbursementID, "employeeId": reimbursement.employeeID, "managerId": reimbursement.managerID, "amount": reimbursement.amount, "message": reimbursement.message, "managerComment": reimbursement.managerComment});

        arr[index] = JSON.parse(pendingReimbursementJSON);        sessionStorage.setItem("pendingReimbursementArray", JSON.stringify(arr));
        index++;

    }
}

function populatePastReimbursementData(responseBody){
    for(let reimbursement of responseBody){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.reimbursementID}</td><td>${reimbursement.employeeID}</td><td>${reimbursement.amount}</td><td>${reimbursement.approval}</td><td>${reimbursement.message}</td><td>${reimbursement.managerComment}</td>`;
        pastReimbursementTableBody.appendChild(tableRow);
    }
}

async function updateApprovedReimbursement(approvedReimbursementId){
    let approvalManagerComment = document.getElementById("managerComment" + approvedReimbursementId).value;
    let arr = sessionStorage.getItem("pendingReimbursementArray");
    let index = 0;
    arrJson = JSON.parse(arr);
    console.log(arrJson);
    let approvalEmployeeID, approvalManagerID, approvalAmount, approvalMessage, approvalReimbursementJSON;
    reimbursementIdArr = [];
    for (jsonIndex in arrJson){
        reimbursementIdArr[index] = arrJson[index].reimbursementId;
        approvalEmployeeID = arrJson[index].employeeId;
        approvalManagerID = arrJson[index].managerId;
        approvalAmount = arrJson[index].amount;
        approvalMessage = arrJson[index].message;

        if(approvedReimbursementId == reimbursementIdArr[index]){
            approvalReimbursementJSON = JSON.stringify({"employeeId": approvalEmployeeID, "managerId": approvalManagerID, "approval": "Approved", "amount": approvalAmount, "message": approvalMessage,"managerComment": approvalManagerComment});
        }
        index++;

        }
    
    console.log(approvalReimbursementJSON);


    let url = "http://127.0.0.1:5000/reimbursement/approve/" + approvedReimbursementId
    let response = await fetch(url, {
        method: "PATCH",
        headers:{"Content-Type": 'application/json'},
        body: approvalReimbursementJSON}).then(response => {return response.json()});
    if(response.reimbursementId != 0){
        window.location.href = "../html/manager_page.html";     
    }   else{
        alert("There was a problem trying to approve the reimbursement");
    }
}

async function updateDeniedReimbursement(deniedReimbursementId){
    let deniedManagerComment = document.getElementById("managerComment" + deniedReimbursementId).value;
    console.log(deniedManagerComment);
    let arrDeny = sessionStorage.getItem("pendingReimbursementArray");
    let indexDeny = 0;
    arrJsonDeny = JSON.parse(arrDeny);
    console.log(arrJsonDeny);
    let deniedEmployeeID, deniedManagerID, deniedAmount, deniedMessage, deniedReimbursementJSON;
    deniedReimbursementIdArr = [];
    for (jsonIndexDeny in arrJsonDeny){
        deniedReimbursementIdArr[indexDeny] = arrJsonDeny[indexDeny].reimbursementId;
        deniedEmployeeID = arrJsonDeny[indexDeny].employeeId;
        deniedManagerID = arrJsonDeny[indexDeny].managerId;
        deniedAmount = arrJsonDeny[indexDeny].amount;
        deniedMessage = arrJsonDeny[indexDeny].message;

        if(deniedReimbursementId == deniedReimbursementIdArr[indexDeny]){
            deniedReimbursementJSON = JSON.stringify({"employeeId": deniedEmployeeID, "managerId": deniedManagerID, "approval": "Denied", "amount": deniedAmount, "message": deniedMessage,"managerComment": deniedManagerComment});
        }
        indexDeny++;

        }
    
    console.log(deniedReimbursementJSON);


    let url = "http://127.0.0.1:5000/reimbursement/deny/" + deniedReimbursementId
    let response = await fetch(url, {
        method: "PATCH",
        headers:{"Content-Type": 'application/json'},
        body: deniedReimbursementJSON}).then(response => {return response.json()});
    if(response.reimbursementId != 0){
        window.location.href = "../html/manager_page.html";     
    }   else{
        alert("There was a problem trying to deny the reimbursement");
    }
}

async function getAllEmployeeReimbursementData(){
    let statisticEmployeeId = document.getElementById("statistic_employee_id");
    sessionStorage.setItem("statistic_employee_id", statisticEmployeeId.value);
    let employeeIdforStat = sessionStorage.statistic_employee_id;
    console.log(employeeIdforStat);



    let url = "http://127.0.0.1:5000/employee/statistics/" + employeeIdforStat;
    let response = await fetch(url);
    if (response.status === 200){
        let body = await response.json();
        ShowChosenStatistic(body);
    }   else{
        alert("There was a problem trying to get the reimbursement information for the statistic: sorry!");
    }
}

async function ShowChosenStatistic(statistics){
    console.log(statistics);
    employeeIdforStat = sessionStorage.statistic_employee_id;
    if (statistics!=null){
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${employeeIdforStat}<td>${statistics[0]}</td><td>${Math.round(statistics[1])}</td><td>${statistics[2]}</td><td>${statistics[3]}</td><td>${statistics[4]}</td>`;
        statisticsBody.appendChild(tableRow, tableRow);


    }else{
        alert("No employee with that ID");
    }

}

function logout(){
    sessionStorage.clear();
    window.location.href = "../html/login_page.html";
}
getAllManagerData();
