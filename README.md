# Health Records App

This app is designed to make it easy to create, review, and share your Personal Health Records.

## Features

- display entries
  - list view
  - filtering
  - gantt view for medications/other
  - maybe graphs
- save records to a database

## Entities

### Database

Tables:

- records
- users

### Backend

API Endpoints:

- **/Users**
  - GET /Users
  - POST /Users
  - DELETE /Users/{id}
  - GET /Users/{id}
  - PUT /Users/{id}
- **/Records**
  - GET /Records
  - POST /Records
  - DELETE /Records/{id}
  - GET /Records/{id}
  - PUT /Records/{id}

### Frontend

Vue.js framework

#### Pages

/  
/RecordForm  
/ViewRecords  
/About

Shown in [[Drawing 2023-02-01 13.17.04.excalidraw]]

#### Classes/

RecordList  
Record  
User
