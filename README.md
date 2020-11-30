# Deployment Guide

## Deployment 
This is the first webpage where the table is shown http://127.0.0.1:5002/home
A patient record can be created for each patient through the "Create Record" button
The "Create Record" buttton links to a preview page which gives 2 formats of download (Word and PDF)
When Word is clicked, the patientRecord.docx which is located in dotnet-azure-fhir-web-api folder is updated to the newest patient data.
When PDF is clicked, a patientRecord.pdf is created in your folder.


## Install Visual Studio Code

- Download and install [Visual Studio Code](https://code.visualstudio.com/)

## Install .NET Core 2.1

- Download and install .NET Core 2.1 [SDK 2.1.803](https://dotnet.microsoft.com/download/dotnet-core/2.1)
- Test your installation by opening a new terminal and running the following command:

    ```bash
    dotnet
    ```

# Running the app

- Clone the project and open it in Visual Studio Code.
- Open the file **appsettings.json**


    ```json
    {
      "Logging": {
        "LogLevel": {
          "Default": "Debug",
          "System": "Information",
          "Microsoft": "Information"
        }
      },
      "Instance": "https://login.microsoftonline.com/{0}",
      "Tenant": "ca254449-06ec-4e1d-a3c9-f8b84e2afe3f",
      "ClientId": "0f6332f4-c060-49fc-bcf6-548982d56569",
      "ClientSecret": "ux@CJAaxCD85A9psm-Wdb?x3/Z4c6gp9",
      "BaseAddress": "https://gosh-fhir-synth.azurehealthcareapis.com",
      "Scope": "https://gosh-fhir-synth.azurehealthcareapis.com/.default"
    }
    ```
- Replace the empty fields with the Azure FHIR API credentials you have been given.
- Save the file.
- Navigate to the directory **dotnet-azure-fhir-web-api** using the terminal inside Visual Studio Code.
- In the terminal, run the following command:

    ```bash
    dotnet run
    ```
- Open a web browser and navigate to [https://localhost:5001/api/Patient/](https://localhost:5001/api/Patient/) to view a list of all patients.


## List of API endpoints

#### Patients

- GET all patients: **/api/Patient**
- GET a patient: **/api/Patient/** *patient ID*
- GET a selected number of pages of patient: **api/pages/** *number of pages*


#### Observations

- GET all observations for a patient: **/api/Observation/** *patient ID*
- GET a single observation for a patient: **api/Observation/single/** *observation ID*
- GET a selected number of pages of observations for a patient: **api/Observation/pages/** *number of pages/patient ID*


# Adding more controllers

The app uses Dependency Injection (DI) design pattern. For more information on how to implement that on .NET Core check [this article](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-2.1)


# Logging and debugging

Check [this article](https://code-maze.com/net-core-web-development-part3/) for an overview of the implemented logging features.
