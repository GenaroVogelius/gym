# Project: Power Gym
![clients side](https://github.com/GenaroVogelius/Power-gym/blob/main/demoFiles/front_power.PNG)

# Description:
The Power Gym project aimed to create an intuitive user interface for customers upon their arrival at the gym. The index page featured a user-friendly interface where customers could enter their DNI (Identification Document Number). Based on this input, the screen would display the following information:

- Green background: If the customer's fee is up to date, the interface would show the number of days left until the next payment is due.
- Red background: If the customer's fee is overdue, the interface would display the date when the fee became overdue.
- Yellow background: If the DNI is not registered in the database, the interface would provide a notification indicating the unavailability of the customer's information.
Additionally, an admin page was developed utilizing the Django admin interface. Customized templates were created to enhance the personalization and functionality. One of the added features was the ability to upload an Excel file to import data directly into the database.

You can find the link of the project here https://power-gym.onrender.com/

# Specifications:

- Backend: The application's backend was built using Django, a powerful Python web framework. Two models were created: one for the gym clients, containing all relevant data needed by the owner, and another for tracking client attendance, including arrival time, date, and fee status. API endpoints were developed using the Django Rest framework to enable smooth data communication.

- Frontend: The application's frontend was developed using React, adhering to the Single Responsibility Principle, which ensured modularity and reusability of components. The DRY (Don't Repeat Yourself) technique was implemented to eliminate redundancy and enhance maintainability. 
