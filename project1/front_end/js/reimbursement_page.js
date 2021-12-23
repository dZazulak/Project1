async function createNewReimbursement(){
    let url = "http://127.0.0.1:5000/new_reimbursement"
    let employeeId = sessionStorage.getItem("employeeID");
    let managerId = document.getElementById("new_reimbursement_manager_id");
    let amount = document.getElementById("new_reimbursement_amount");
    let approval = "Pending";
    let message = document.getElementById("new_reimbursement_message");
    let manager_comment = "";

    sessionStorage.setItem("new_reimbursement_employeeId", employeeId.value);
    sessionStorage.setItem("new_reimbursement_managerId", managerId.value);
    sessionStorage.setItem("new_reimbursement_amount", amount.value);
    sessionStorage.setItem("new_reimbursement_message", message.value);

    let createReimbursementJSON = JSON.stringify({"reimbursementId": 0, "employeeId": parseInt(employeeId), "managerId": parseInt(managerId.value), "amount": parseInt(amount.value), "approval": approval, "message": message.value, "managerComment": manager_comment});
    console.log(createReimbursementJSON);

    let response = await fetch(url, {
        method: "POST",
        headers:{"Content-Type": 'application/json'},
        body:createReimbursementJSON}).then(response => {return response.json()});

    if (response.amount > 0){
        window.location.href = "../html/employee_page.html";
    }
    else{
        alert("There was an issue");

    }
}

function returnToHomePage(){
    window.location.href="../html/employee_page.html";
}