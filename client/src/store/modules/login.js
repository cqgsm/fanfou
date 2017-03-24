import * as types from '../mution-types'

// initial state
const state = {
  user: {},
  token: null
}

// actions
// const actions = {
//   getAllProducts ({ commit }) {
//     shop.getProducts(products => {
//       commit(types.RECEIVE_PRODUCTS, { products })
//     })
//   }
// }

// mutations
const mutations = {
  [types.USER_LOGIN] (state, data) {
    localStorage.setItem('token', data.token);
    state.token = data.token;
  },

  [types.USER_LOGOUT] (state) {
    localStorage.removeItem('token');
    state.token = null
  }
}

export default {
  state,
  actions,
  mutations
}