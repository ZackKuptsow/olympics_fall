import axiosAPI, { setNewHeaders } from './axiosApi';

export async function getEventsApi() {
	const response = await axiosAPI.get('/get/events/');

	return response.data;
}
