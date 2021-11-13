import axiosAPI, { setNewHeaders } from './axiosApi';

export async function getTeamsApi() {
	const response = await axiosAPI.get('/get/teams/');

	return response.data;
}
