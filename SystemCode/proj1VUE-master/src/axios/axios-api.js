import axiosService from "./axios-request";
// const BASE = 'http://192.168.1.84:8000'
const BASE = 'http://127.0.0.1:8000'
// const BASE = 'http://192.168.1.19:8000'


// 下面是POST形式
export const getRecommendSchool = data => {
  return axiosService({
    url: BASE + `/getRecommendSchool/`, // get Recommend School List
    method: "post",
    data
  });
};


export const getSchoolDetail = data => {
  return axiosService({
    url: BASE + `/getSchoolDetail/`, // get Recommend School Detail Info
    method: "post",
    data
  });
};

export const getEvaluateLevel = data => {
  return axiosService({
    url: BASE + `/getEvaluateLevel/`, // get Recommend School Detail Info
    method: "post",
    data
  });
};

export const getLevelDetail = data => {
  return axiosService({
    url: BASE + `/getLevelDetail/`, // get Recommend School Detail Info
    method: "post",
    data
  });
};


export const putUsersInfo = data => {
  return axiosService({
    url: BASE + `/putUsersInfo/`, // pass all data the user typed to back end
    method: "post",
    data
  });
};



