function createProjectCard(projectID, lastUpdate, criticality, priority, status, description, riskRating, customerFeedback, budget, milestones) {
    var cardContainer = document.getElementById("projectCards");

    var card = document.createElement("div");
    card.classList.add("project-card");

    var title = document.createElement("h2");
    title.textContent = "Project #" + projectID;
    card.appendChild(title);

    var info = document.createElement("div");
    info.classList.add("project-info");

    var lastUpdatePara = document.createElement("p");
    lastUpdatePara.textContent = "Last Update: " + lastUpdate;
    info.appendChild(lastUpdatePara);

    var criticalityPara = document.createElement("p");
    criticalityPara.textContent = "Criticality: " + criticality;
    info.appendChild(criticalityPara);

    var priorityPara = document.createElement("p");
    priorityPara.textContent = "Priority: " + priority;
    info.appendChild(priorityPara);

    var statusPara = document.createElement("p");
    statusPara.textContent = "Status: " + status;
    info.appendChild(statusPara);

    var descriptionPara = document.createElement("p");
    descriptionPara.textContent = "Description: " + description;
    info.appendChild(descriptionPara);

    var riskRatingPara = document.createElement("p");
    riskRatingPara.textContent = "Risk Rating: " + riskRating;
    info.appendChild(riskRatingPara);

    var customerFeedbackPara = document.createElement("p");
    customerFeedbackPara.textContent = "Customer Feedback: " + customerFeedback;
    info.appendChild(customerFeedbackPara);

    var budgetPara = document.createElement("p");
    budgetPara.textContent = "Budget: $" + budget;
    info.appendChild(budgetPara);

    var milestonesPara = document.createElement("p");
    milestonesPara.textContent = "Milestones: " + milestones;
    info.appendChild(milestonesPara);

    card.appendChild(info);

    cardContainer.appendChild(card);
}

// Remove the first project card
var firstCard = document.querySelector('.project-card');
if (firstCard) {
    firstCard.remove();
}

// Example project cards
createProjectCard(1, "2024-06-01", "High", "High", "Active", "Lorem ipsum dolor sit amet.", "Medium", "Positive", 5000, "Design, Development, Testing");
createProjectCard(2, "2024-05-15", "Medium", "Medium", "In Progress", "Consectetur adipiscing elit.", "Low", "Neutral", 8000, "Planning, Execution, Evaluation");
createProjectCard(3, "2024-06-10", "Low", "Low", "Completed", "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "High", "Negative", 3000, "Research, Prototype, Launch");