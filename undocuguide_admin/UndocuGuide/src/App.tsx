// in src/App.js
import * as React from "react";
import { Admin, Resource } from 'react-admin';
import restProvider from 'ra-data-simple-rest'
import ScholarshipList from './components/ScholarshipList'


// const dataProvider = simpleRestProvider('http://path.to.my.api/');

const App = () => (
    // <Admin dataProvider={dataProvider}>
    //     <Resource name="scholarships" list={PostList} />
    // </Admin>
    <Admin dataProvider={restProvider('http://127.0.0.1:5000/')}>
        <Resource name="scholarships" list={ScholarshipList}/>
    </Admin>
);

export default App;
