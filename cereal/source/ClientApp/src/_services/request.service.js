import { authHeader, handleResponse } from '../_helpers';

export const requestService = {
    requestCereal,
    getCerealRequests
};

function requestCereal(json) {
    const requestOptions = {
        method: 'POST',
        headers: authHeader(),
        body: JSON.stringify({ json })
    };
    return fetch('/requests', requestOptions).then(handleResponse);
}

function getCerealRequests() {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };
    return fetch('/requests', requestOptions).then(handleResponse);
}