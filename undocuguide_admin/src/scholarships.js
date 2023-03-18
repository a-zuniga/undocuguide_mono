import React from 'react';
import { List, Datagrid, TextField, DateField, NumberField, EditButton, DeleteButton, Edit, SimpleForm, TextInput, NumberInput, DateInput, Create } from 'react-admin';

export const ScholarshipList = props => (
    <List {...props}>
        <Datagrid>
            <TextField source="_id" label="ID" />
            <TextField source="name" />
            <TextField source="description" />
            <NumberField source="amount" />
            <DateField source="deadline" />
            <TextField source="url" />
            <EditButton />
            <DeleteButton />
        </Datagrid>
    </List>
);

export const ScholarshipEdit = props => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput disabled source="_id" label="ID" />
            <TextInput source="name" />
            <TextInput multiline source="description" />
            <NumberInput source="amount" />
            <DateInput source="deadline" />
            <TextInput source="url" />
        </SimpleForm>
    </Edit>
);

export const ScholarshipCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="name" />
            <TextInput multiline source="description" />
            <NumberInput source="amount" />
            <DateInput source="deadline" />
            <TextInput source="url" />
        </SimpleForm>
    </Create>
);
