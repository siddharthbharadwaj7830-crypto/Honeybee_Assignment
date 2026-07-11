import "./App.css";
import { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  PieChart,
  Pie,
  Cell,
  Legend,
} from "recharts";

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042"];

function App() {
  const [listings, setListings] = useState([]);
  const [citySummary, setCitySummary] = useState([]);
  const [categorySummary, setCategorySummary] = useState([]);
  const [sourceSummary, setSourceSummary] = useState([]);
  const [city, setCity] = useState("");
const [category, setCategory] = useState("");
const [businessName, setBusinessName] = useState("");
const [formCategory, setFormCategory] = useState("");
const [formCity, setFormCity] = useState("");
const [address, setAddress] = useState("");
const [phone, setPhone] = useState("");
const [source, setSource] = useState("");

function loadData() {
  fetch("http://127.0.0.1:8000/listings")
    .then((response) => response.json())
    .then((data) => setListings(data));

  fetch("http://127.0.0.1:8000/dashboard/city")
    .then((response) => response.json())
    .then((data) => setCitySummary(data));

  fetch("http://127.0.0.1:8000/dashboard/category")
    .then((response) => response.json())
    .then((data) => setCategorySummary(data));

  fetch("http://127.0.0.1:8000/dashboard/source")
    .then((response) => response.json())
    .then((data) => setSourceSummary(data));
} 
useEffect(() => {
  loadData();
}, []);
  function searchListings() {
  fetch(
    `http://127.0.0.1:8000/listings?city=${city}&category=${category}`
  )
    .then((response) => response.json())
    .then((data) => setListings(data))
    .catch((error) => console.log(error));
}function addListing() {
  fetch("http://127.0.0.1:8000/listings", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      business_name: businessName,
      category: formCategory,
      city: formCity,
      address: address,
      phone: phone,
      source: source,
    }),
  })
    .then((response) => response.json())
    .then(() => {
      alert("Listing Added Successfully!");
      setBusinessName("");
setFormCategory("");
setFormCity("");
setAddress("");
setPhone("");
setSource("");

   loadData(); 
    })
    .catch((error) => console.log(error));
}

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>🐝 Honeybee Business Listings Dashboard</h1>

      <div style={{ display: "flex", gap: "20px", marginBottom: "30px" }}>
        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            borderRadius: "10px",
          }}
        >
          <h3>Total Listings</h3>
          <h2>{listings.length}</h2>
        </div>

        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            borderRadius: "10px",
          }}
        >
          <h3>Cities</h3>
          <h2>{citySummary.length}</h2>
        </div>

        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            borderRadius: "10px",
          }}
        >
          <h3>Categories</h3>
          <h2>{categorySummary.length}</h2>
        </div>

        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            borderRadius: "10px",
          }}
        >
          <h3>Sources</h3>
          <h2>{sourceSummary.length}</h2>
        </div>
      </div>

      <h2>City Wise Businesses</h2>

      <BarChart width={600} height={300} data={citySummary}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" fill="#8884d8" />
      </BarChart>

      <br />

      <h2>Category Distribution</h2>

      <PieChart width={500} height={300}>
        <Pie
          data={categorySummary}
          dataKey="count"
          nameKey="name"
          outerRadius={100}
          label
        >
          {categorySummary.map((entry, index) => (
            <Cell
              key={index}
              fill={COLORS[index % COLORS.length]}
            />
          ))}
        </Pie>

        <Tooltip />
        <Legend />
      </PieChart>

      <div style={{ marginBottom: "20px" }}>
  <input
    type="text"
    placeholder="Enter City"
    value={city}
    onChange={(e) => setCity(e.target.value)}
    style={{
      padding: "8px",
      marginRight: "10px"
    }}
  />

  <input
    type="text"
    placeholder="Enter Category"
    value={category}
    onChange={(e) => setCategory(e.target.value)}
    style={{
      padding: "8px",
      marginRight: "10px"
    }}
  />

  <button
    onClick={searchListings}
    style={{
      padding: "8px 15px",
      cursor: "pointer"
    }}
  >
    Search
  </button>
</div>
      <h2>Add New Business</h2>

<div style={{ marginBottom: "20px" }}>
  <input
    type="text"
    placeholder="Business Name"
    value={businessName}
    onChange={(e) => setBusinessName(e.target.value)}
  />

  <input
    type="text"
    placeholder="Category"
    value={formCategory}
    onChange={(e) => setFormCategory(e.target.value)}
  />

  <input
    type="text"
    placeholder="City"
    value={formCity}
    onChange={(e) => setFormCity(e.target.value)}
  />

  <input
    type="text"
    placeholder="Address"
    value={address}
    onChange={(e) => setAddress(e.target.value)}
  />

  <input
    type="text"
    placeholder="Phone"
    value={phone}
    onChange={(e) => setPhone(e.target.value)}
  />

  <input
    type="text"
    placeholder="Source"
    value={source}
    onChange={(e) => setSource(e.target.value)}
  />

  <button onClick={addListing}>
    Add Listing
  </button>
</div>
      <h2>Business Listings</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Business Name</th>
            <th>Category</th>
            <th>City</th>
            <th>Phone</th>
            <th>Source</th>
          </tr>
        </thead>

        <tbody>
          {listings.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.business_name}</td>
              <td>{item.category}</td>
              <td>{item.city}</td>
              <td>{item.phone}</td>
              <td>{item.source}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;