# VACon_rest
REST API combining Steam profile information and VAC Status

/player/***STEAMID*** returns a JSON object containing information about the player,
/friendslist/***STEAMID*** returns, for each friend of the Steam ID, a JSON list of objects that each contain:

<ul>
<li>Steam ID</li>
<li>Persona Name</li>
<li>Community URL</li>
<li>Avatar URL</li>
<li>VAC Status</li>
</ul>

This is currently running on a server at http://kimsufi.darrenoneill.ie/VACon/

for example, with my own steam ID:<br>
http://kimsufi.darrenoneill.ie/VACon/player/76561197986539195
http://kimsufi.darrenoneill.ie/VACon/friendslist/76561197986539195

