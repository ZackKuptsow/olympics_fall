import { GET_TEAMS } from './types';
import { getTeamsApi } from '../../components/api/getTeamsApi';

// export function getTeams() {
// 	return async function (dispatch) {
// 		try {
// 			const response = await getTeamsApi();
// 			// dispatch(response.data);
// 			return { type: GET_TEAMS, response };
// 		} catch {
// 			console.log('Error obtaining teams from API.');
// 		}
// 	};
// }

// export const getTeams = formValues => async (dispatch, getState) => {
export const getTeams = () => async dispatch => {
	console.log('getTeams action');
	// const { userId } = getState().auth;
	const response = await streams.post('/get/teams/');

	dispatch({ type: GET_TEAMS, payload: response.data });
	// do some programatic navigation to get the user back to the root route
	history.push('/');
};
