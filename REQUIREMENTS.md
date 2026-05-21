# 🎮 Play&Win — Gaming App Requirements

## App Overview
- **App Name:** Play&Win
- **Platform:** Android (Single App)
- **Games:** Ludo (4 players) + Chase/Snake & Ladder (2 players)
- **Features:** Real-time multiplayer, Chat, Global matchmaking

---

## 1. Games

### 🎲 Ludo
- 4 players (2 local + 2 online OR all 4 online)
- Standard Ludo rules
- Dice roll animation
- Token movement with safe zones
- Win condition: All 4 tokens reach home

### 🏃 Chase (Snake & Ladder)
- 2 players only
- Standard Snake & Ladder board (100 squares)
- Dice roll per turn
- Snakes bring you down, Ladders take you up
- Win condition: First to reach square 100

---

## 2. Multiplayer & Matchmaking

### Global Search / Matchmaking
- Players set a **entry cost** (e.g. ₹10, ₹50, ₹100)
- System matches players with **same cost**
- Matchmaking queue with timer
- Room creation (public/private)
- Private room: share 6-digit room code

---

## 3. Chat System
- **In-game chat** for both Ludo & Chase rooms
- Group chat per game room
- Emoji support 😄🎲🏆
- Chat history during game session
- Mute/Block player option

---

## 4. User System
- Register / Login (Email + Google)
- Player profile: avatar, username, win/loss stats
- Wallet: add money, withdraw winnings
- Transaction history

---

## 5. Tech Stack (Android)

| Layer        | Technology              |
|---|---|
| Frontend     | Kotlin + Jetpack Compose |
| Backend      | Firebase Realtime DB     |
| Auth         | Firebase Auth            |
| Chat         | Firebase Firestore       |
| Payments     | Razorpay SDK             |
| Game Logic   | Custom Kotlin classes    |
| Matchmaking  | Firebase Cloud Functions |

---

## 6. Screens

1. Splash Screen
2. Login / Register
3. Home Dashboard
4. Game Selection (Ludo / Chase)
5. Matchmaking / Room Join
6. Ludo Game Board
7. Chase Game Board
8. In-game Chat
9. Wallet & Payments
10. Profile & Stats
11. Leaderboard
