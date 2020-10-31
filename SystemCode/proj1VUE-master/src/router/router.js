import App from '../App'
import personalInfo from "../components/personalInfo";
import personalComp from "../components/personalComp";
import schoolDetail from "../components/schoolDetail";
import results from "../components/recommendresults";
import country from "../components/country";
export default [{
    path: '/',
    component: App,
    children: [
      {
        path: '',
        component: r => require.ensure([], () => r(require('../page/home')), 'home')
    },
      {
        path: '/schoolDetail',
        name:'schoolDetail',
        component: schoolDetail
    },
      {
        path: '/score',
        component: r => require.ensure([], () => r(require('../page/score')), 'score')
    },
      {
        path: '/recommendresults',
        name:'results',
        component: results,
      },
      {
      path: '/personalInfo',
      name:'personalInfo',
      component: personalInfo,
    },
      {
      path: '/personalComp',
      name:'personalComp',
      component: personalComp
    },
      {
        path: '/country',
        name:'country',
        component: country
      },]
}]
