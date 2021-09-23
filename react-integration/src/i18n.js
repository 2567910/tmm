import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import axios from 'axios'
import HttpApi from 'i18next-http-backend';


axios.defaults.baseURL = 'https://old.lukasseyfarth.com'

axios.defaults.headers = {
    'x-apikey': '59a7ad19f5a9fa0808f11931',
    'Access-Control-Allow-Credentials':true,
    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
  }


const getTranslationsFromServer=async(locale)=> {
    axios.get(locale).then(response => {
        return response.data
      }).catch(error => {
        console.log(error)
      })

    // return await axiosInstance().get('/translate-data/get', { params: { lang: locale } })
    //   .then((response) => { return response.data })
    //   .catch((error) => { console.log(error); });
}


let options = {
    loadPath:
      '/tmm/{{lng}}.json',
      request: (options, url, payload, callback) => {
        try {
          const [lng] = url.split('|');
          getTranslationsFromServer(lng).then((response) => {
            callback(null, {
              data: response,
              status: 200,
            });
          });
        } catch (e) {
          console.error(e);
          callback(null, {
            status: 500,
          });
        }
      },
    crossDomain: true,

    // allow credentials on cross domain requests
    withCredentials: true,
  }


i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .use(HttpApi)
  .init({
    debug: true,
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false, // not needed for react as it escapes by default
    },
    backend: options,
  });

export default i18n;