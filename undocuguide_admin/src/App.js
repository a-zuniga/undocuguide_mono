import { Admin, Resource } from 'react-admin';
import { FirebaseAuthProvider } from 'react-admin-firebase';
import {auth, googleProvider} from './firebase'
import { ScholarshipList, ScholarshipCreate, ScholarshipEdit } from './scholarships';
import dataProvider from './dataProvider';
import firebaseConfig from './firebase';
import CustomLoginPage from './CustomLoginPage';

const firebaseAuthProvider = FirebaseAuthProvider(firebaseConfig, {userProfilePath: '/users/'});

const App = () => (
  <Admin dataProvider={dataProvider} authProvider={firebaseAuthProvider} loginPage={CustomLoginPage}>
    <Resource name="scholarships" list={ScholarshipList} create={ScholarshipCreate} edit={ScholarshipEdit} />
  </Admin>
);

export default App;