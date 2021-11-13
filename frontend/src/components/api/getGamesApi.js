import axiosAPI, { setNewHeaders } from './axiosApi';

export async function getGamesApi() {
	const response = await axiosAPI.get('/get/games/');

	return response.data;
}
