import axiosAPI, { setNewHeaders } from './axiosApi';

export async function getPlayersApi() {
	const response = await axiosAPI.get('/get/players/');

	return response.data;
}
