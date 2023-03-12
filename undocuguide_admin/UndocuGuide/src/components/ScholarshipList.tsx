import React from "react";
import {
    List, 
    Datagrid,
    TextField,
    DateField,
    EditButton,
    DeleteButton
} from "react-admin"

const ScholarshipList = (props) => (
    <List {...props}>
        <Datagrid>
            <TextField source="name" />
            <TextField source="description" />
            <TextField source="amount" />
            <TextField source="deadline" />
            <TextField source="url" />
            <EditButton />
            <DeleteButton />
        </Datagrid>
    </List>
);

export default ScholarshipList;