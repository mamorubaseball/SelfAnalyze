// apiを取得するコード

import { CSRF_TOKEN } from "./csrf_token.js";

function handleResponse(response){
    if (response.status === 204){
        return 'エラー';
    }else if (response.status === 404){
        return null;
    }else{
        return response.json();
    }
}

//fetch apiの仕様の確認が必要
function apiService(endpoint,method,data){
    const config={
        method: method || 'get', //method or get→methodがない場合はgetを使用。
        body: data !== undefined ? JSON.stringify(data) :null,
        headers:{
            'content-type':'application/json',
            'X-CSRFTOKEN':CSRF_TOKEN
        }
    };
    return fetch(endpoint,config).then(handleResponse);
}
export { apiService };