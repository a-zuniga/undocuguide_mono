import React from 'react';
import { Admin, Resource } from 'react-admin';
import { emailAndPasswordAuthProvider } from 'react-admin-firebase';
import auth from './firebase';
import { ScholarshipList, ScholarshipCreate, ScholarshipEdit } from './scholarships';
import dataProvider from './dataProvider';
import CustomLoginPage from './CustomLoginPage';

const firebaseAuthProvider = emailAndPasswordAuthProvider(auth, {userProfilePath: '/users/'});

const App = () => (
  <Admin dataProvider={dataProvider} authProvider={firebaseAuthProvider} loginPage={CustomLoginPage}>
    <Resource name="scholarships" list={ScholarshipList} create={ScholarshipCreate} edit={ScholarshipEdit} />
  </Admin>
);

export default App;
