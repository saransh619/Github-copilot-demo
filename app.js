//fetchapi
import fetch from 'fetch-api';
let fetchApi = fetch('https://fakerapi.it/api/v1/%7Bresource%7D');
fetchApi.then(function(response) {
  console.log(response.data);
}
);

