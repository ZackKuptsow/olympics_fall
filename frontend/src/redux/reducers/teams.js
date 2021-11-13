import * as types from '../actions/types';

export default function teamsReducer(state = {}, action) {
	switch (action.type) {
		case types.GET_TEAMS:
			console.log('reducer');
			return action;
		default:
			return state;
	}
}
