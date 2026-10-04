import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Home = () => {
  const [user, setUser] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/', { withCredentials: true })
      .then(res => setUser(res.data.user))
      .catch(err => {
        console.error(err);
        setError("Not authenticated or server error.");
      });
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Manga Reader</h1>
      {error && <p className="text-red-500">{error}</p>}
      {user ? (
        <p>Welcome back, {user.username}!</p>
      ) : (
        <p>Loading user info...</p>
      )}
    </div>
  );
};

export default Home;
