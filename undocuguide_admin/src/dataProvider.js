import { fetchUtils } from 'react-admin';
import simpleRestProvider from 'ra-data-simple-rest';

const apiUrl = 'http://localhost:8000';

const httpClient = async (url, options = {}) => {
    if (!options.headers) {
        options.headers = new Headers({ Accept: 'application/json' });
    }
    const response = await fetchUtils.fetchJson(url, options);
    return response;
};

const dataProvider = simpleRestProvider(apiUrl, httpClient);

export default dataProvider;
