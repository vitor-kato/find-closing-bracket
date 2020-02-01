import axios from 'axios';
const API_URL = 'http://0.0.0.0:8000';

export default class bracketService {

    getBrackets () {
        const url = `${API_URL}/api/v1/bracket/`;
        return axios.get(url).then(response => response.data);
    }
    getBracketByURL (link) {
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getBracket (id) {
        const url = `${API_URL}/api/v1/bracket/${id}`;
        return axios.get(url).then(response => response.data);
    }
    deleteBracket (bracket) {
        const url = `${API_URL}/api/v1/bracket/${bracket.id}`;
        return axios.delete(url);
    }
    createBracket (bracket) {
        const url = `${API_URL}/api/v1/bracket/`;
        return axios.post(url, bracket);
    }
    updateBracket (bracket) {
        const url = `${API_URL}/api/v1/bracket/${bracket.id}/`;
        return axios.put(url, bracket);
    }
}