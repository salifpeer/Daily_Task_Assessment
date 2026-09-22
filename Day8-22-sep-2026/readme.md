<h1>Daily Task Assessment - Day 8</h1>

<h3>Authentication, Sessions, Cookies, JWT and OAuth 2.0</h3>

<p>
Today I learned about <b>authentication</b>, <b>authorization</b>, <b>sessions</b>, 
<b>cookies</b>, <b>JWT </b>, and <b>OAuth 2.0</b>. 
I understood the difference between <b>stateful</b> and <b>stateless authentication</b>.
</p>

<br>

<h3>1.Authentication and Authorization</h3>

<p>
Learned the difference between <b>authentication</b> and <b>authorization</b>.
Authentication is used to verify the identity of a user, while authorization determines 
what an authenticated user is allowed to access or perform.
</p>

<h3>2. Stateful Authentication - Sessions and Cookies</h3>

<p>
Learned about stateful authentication using sessions and cookies. 
In this approach, the server maintains information about the user's login session.
</p>

<p>
After successful login, the server creates a session and sends a session identifier 
to the browser through a cookie. The browser sends the cookie with subsequent 
requests, allowing the server to identify the user's session.
</p>

<p>
The server therefore needs to maintain the user's session information, which makes 
this approach stateful.
</p>

<h3>3. Stateless Authentication - JWT</h3>

<p>
Learned about stateless authentication using JWT. In this approach, the 
server creates a signed JSON Web Token after successful authentication.
</p>

<h3>4. OAuth 2.0</h3>

<p>
Learned the basics of <b>OAuth 2.0</b> and understood how it allows an application 
to obtain permission to access protected resources on behalf of a user without 
sharing the user's password with that application.
</p>



<h3>5. Stateful vs Stateless Authentication</h3>

<p>
Understood the basic difference between stateful and stateless authentication.
</p>

<p>
<b>Stateful:</b> The server maintains the user's session information. 
Sessions and cookies are commonly used together.
</p>

<p>
<b>Stateless:</b> The server does not need to maintain a login session for each 
client. The client sends authentication information, such as an access token, 
with each request.
</p>

<br>