import React from 'react';
import { useState } from 'react';
import { Link } from 'react-router-dom';

import { getTeamsApi } from '../api/getTeamsApi';
import { getPlayersApi } from '../api/getPlayersApi';

const getTeams = async () => {
	const response = await getTeamsApi();

	return response;
};

const getPlayers = async () => {
	const response = await getPlayersApi();

	return response;
};

const makeTeamsPairing = () => {
	const teams = getTeams();
	let pairing = {};
	for (let team in teams) {
		pairing[team['id']] = team['name'];
	}

	return pairing;
};

const makeTeams = () => {
	const teams = makeTeamsPairing();
	console.log(teams);
	const players = getPlayers();
	let teamList = {};

	// for (let player of players) {
	// 	if
	// }
	return 'toast';
};

const Teams = () => {
	// const [teams, setTeams] = useState(getTeams());
	// const [players, setPlayers] = useState(getPlayers());
	const [teams, setTeams] = useState(makeTeams());

	// const teamNames = teams.map((t) => t.name)
	// console.log(teamNames)

	// const renderTeams = (teams, players) => {
	// 	const
	// 	for(player in players) {
	// 		if
	// 	}
	// }

	return (
		<div>
			<div className="ui three item menu">
				<Link to="/" className="item">
					Dashboard
				</Link>
				<Link to="/teams" className="active item">
					Teams
				</Link>
				<Link to="/leaderboard" className="item">
					Leaderboard
				</Link>
			</div>
			<div className="ui one column doubling stackable grid container">
				{teams}
			</div>
		</div>
	);
};

export default Teams;
