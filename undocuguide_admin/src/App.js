import * as React from 'react';
import { Admin, Resource } from 'react-admin';
import { ScholarshipList, ScholarshipEdit, ScholarshipCreate } from './scholarships';
import dataProvider from './dataProvider';

const App = () => (
  <Admin dataProvider={dataProvider}>
    <Resource
      name="scholarships"
      list={ScholarshipList}
      edit={ScholarshipEdit}
      create={ScholarshipCreate}
    />
  </Admin>
);

export default App;