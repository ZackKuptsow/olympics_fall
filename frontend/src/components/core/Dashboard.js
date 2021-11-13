import React from 'react';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import { getGamesApi } from '../api/getGamesApi';
import { getTeamsApi } from '../api/getTeamsApi';
import { getEventsApi } from '../api/getEventsApi';

const getGames = async () => {
	const response = await getGamesApi();

	return response;
};

const getTeams = async () => {
	const response = await getTeamsApi();

	return response;
};

const getEvents = async () => {
	const response = await getEventsApi();

	return response;
};

const Dashboard = () => {
	const [teamsApi, setTeamsApi] = useState();
	const [eventsApi, setEventsApi] = useState();
	const [games, setGames] = useState();
	const [teams, setTeams] = useState();
	const [events, setEvents] = useState();
	const [renderOnDeck, setRenderOnDeck] = useState();
	const [renderPlaying, setRenderPlaying] = useState();

	useEffect(() => {
		let isMounted = true;
		getTeamsApi().then(t => {
			if (isMounted) setTeamsApi(t);
		});
		return () => {
			isMounted = false;
		};
	}, []);

	useEffect(() => {
		let isMounted = true;
		getGames().then(t => {
			if (isMounted) setGames(t);
		});
		return () => {
			isMounted = false;
		};
	}, []);

	useEffect(() => {
		let isMounted = true;
		getEventsApi().then(e => {
			if (isMounted) setEventsApi(e);
		});
		return () => {
			isMounted = false;
		};
	}, []);

	useEffect(() => {
		const newTeams = {};

		if (teamsApi) {
			teamsApi.map(team => {
				newTeams[team['id']] = team['name'];
			});
			setTeams(newTeams);
		}
	}, [teamsApi]);

	useEffect(() => {
		const newEvents = {};

		if (eventsApi) {
			eventsApi.map(event => {
				newEvents[event['id']] = event['name'];
			});
			setEvents(newEvents);
		}
	}, [eventsApi]);

	useEffect(() => {
		if (games && events) {
			setRenderOnDeck(
				games.map(game => {
					if (game['on_deck']) {
						return (
							<div key={game['id']}>
								<h3>
									{events[game['event']]} Round{' '}
									{game['round']}
								</h3>
								<h4>
									{teams[game['first_team']]} vs.{' '}
									{teams[game['second_team']]}
								</h4>
								<hr />
							</div>
						);
					}
				})
			);
		}
	}, [games, events]);

	useEffect(() => {
		if (games && events) {
			setRenderPlaying(
				games.map(game => {
					if (game['is_playing']) {
						return (
							<div key={game['id']}>
								<h3>
									{events[game['event']]} Round{' '}
									{game['round']}
								</h3>
								<h4>
									{teams[game['first_team']]} vs.{' '}
									{teams[game['second_team']]}
								</h4>
								<hr />
							</div>
						);
					}
				})
			);
		}
	}, [games, events]);

	return (
		<div>
			<div className="ui three item menu">
				<Link to="/" className="active item">
					Dashboard
				</Link>
				<Link to="/teams" className="item">
					Teams
				</Link>
				<Link to="/leaderboard" className="item">
					Leaderboard
				</Link>
			</div>
			<div className="column">
				<h1>On Deck</h1>
				<div>{games ? renderOnDeck : <p>Loading...</p>}</div>
			</div>
			<div className="column">
				<h1>Playing</h1>
				<div>{games ? renderPlaying : <p>Loading...</p>}</div>
			</div>
		</div>
	);
};

export default Dashboard;
