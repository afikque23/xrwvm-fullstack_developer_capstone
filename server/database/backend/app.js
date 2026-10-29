const express = require('express');
const app = express();
const port = 3030;

app.use(express.json());

// Sample data
const dealerships = [
  { id: 1, city: "Wichita", state: "Kansas", st: "KS", zip: "67201", lat: "37.6922", long: "-97.3375", short_name: "Kansas Best Cars", full_name: "Best Cars of Kansas" },
  { id: 2, city: "Salina", state: "Kansas", st: "KS", zip: "67401", lat: "38.8403", long: "-97.6114", short_name: "Salina Best Cars", full_name: "Best Cars of Salina Kansas" },
  { id: 3, city: "Los Angeles", state: "California", st: "CA", zip: "90001", lat: "34.0522", long: "-118.2437", short_name: "LA Best Cars", full_name: "Best Cars of Los Angeles" },
  { id: 4, city: "San Francisco", state: "California", st: "CA", zip: "94102", lat: "37.7749", long: "-122.4194", short_name: "SF Best Cars", full_name: "Best Cars of San Francisco" },
  { id: 5, city: "Chicago", state: "Illinois", st: "IL", zip: "60601", lat: "41.8781", long: "-87.6298", short_name: "Chicago Best Cars", full_name: "Best Cars of Chicago" },
  { id: 6, city: "Houston", state: "Texas", st: "TX", zip: "77001", lat: "29.7604", long: "-95.3698", short_name: "Houston Best Cars", full_name: "Best Cars of Houston" },
  { id: 7, city: "Phoenix", state: "Arizona", st: "AZ", zip: "85001", lat: "33.4484", long: "-112.0740", short_name: "Phoenix Best Cars", full_name: "Best Cars of Phoenix" },
  { id: 8, city: "New York", state: "New York", st: "NY", zip: "10001", lat: "40.7128", long: "-74.0060", short_name: "NY Best Cars", full_name: "Best Cars of New York" }
];

const reviews = [
  { id: 1, name: "Berkly Shepley", dealership: 1, review: "Fantastic services! The staff was very friendly and helpful. I am very satisfied with my purchase.", purchase: true, purchase_date: "02/16/2021", car_make: "Nissan", car_model: "Qashqai", car_year: 2021 },
  { id: 2, name: "John Smith", dealership: 1, review: "Great experience! Would definitely recommend to others.", purchase: true, purchase_date: "03/10/2021", car_make: "Toyota", car_model: "Corolla Cross", car_year: 2022 },
  { id: 3, name: "Mike Johnson", dealership: 2, review: "Very good service. The car was in excellent condition.", purchase: false, purchase_date: "01/05/2022", car_make: "Ford", car_model: "Mustang", car_year: 2022 },
  { id: 4, name: "Emma Wilson", dealership: 3, review: "Amazing experience! The team in LA was incredibly helpful.", purchase: true, purchase_date: "04/20/2022", car_make: "Audi", car_model: "A4", car_year: 2022 },
  { id: 5, name: "Carlos Garcia", dealership: 3, review: "Good selection of cars. Prices were fair.", purchase: false, purchase_date: "05/15/2022", car_make: "Mercedes", car_model: "C-Class", car_year: 2023 }
];

// Routes
app.get('/fetchDealers', (req, res) => {
  res.json(dealerships);
});

app.get('/fetchDealers/:state', (req, res) => {
  const state = req.params.state;
  const filtered = dealerships.filter(d => d.state.toLowerCase() === state.toLowerCase() || d.st.toLowerCase() === state.toLowerCase());
  res.json(filtered);
});

app.get('/fetchDealer/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const dealer = dealerships.find(d => d.id === id);
  res.json(dealer ? [dealer] : []);
});

app.get('/fetchReviews/dealer/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const dealerReviews = reviews.filter(r => r.dealership === id);
  res.json(dealerReviews);
});

app.post('/insert_review', (req, res) => {
  const review = { id: reviews.length + 1, ...req.body };
  reviews.push(review);
  res.json({ status: 200, message: "Review added successfully" });
});

app.listen(port, () => {
  console.log(`Dealer service running on port ${port}`);
});
