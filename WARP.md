# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a personal bio/portfolio website featuring real-time Discord and Spotify integration. It's a static HTML/CSS/JavaScript site that displays live status information from Discord and Spotify using the Lanyard API.

## Development Commands

Since this is a static website with no build system:

### Local Development
```powershell
# Serve locally using Python (if available)
python -m http.server 8000

# Or using Node.js http-server
npx http-server .

# Or simply open in browser
start index.html  # Windows
```

### File Watching/Live Reload
```powershell
# If using live-server for development
npx live-server .
```

### Testing
Since this is a frontend-only project:
- Open `index.html` in multiple browsers to test compatibility
- Test with browser dev tools' device simulation for responsive design
- Check console for any JavaScript errors

## Code Architecture

### File Structure
```
bio-main/
├── index.html          # Main HTML structure and layout
├── script.js          # All JavaScript functionality and API integrations  
├── style.css          # Complete CSS styling with animations and responsive design
├── junkie.mp3         # Background music file
└── README.md          # Basic project description
```

### High-Level Architecture

**Single-Page Application (SPA)**
The site is a single-page application with multiple states:
1. **Entry Page**: Initial landing with "Click to Enter" button
2. **Main Site**: Full bio page with widgets and profile information

**Key Architectural Patterns:**

1. **Module-Based JavaScript**: Functions are organized by feature area:
   - Audio management (`initializeEntryPage`, `toggleAudio`)
   - Real-time status updates (`updateDiscordStatus`, `updateSpotifyStatus`) 
   - UI interactions (`initializeCursor`, `initializeSocialLinks`)
   - Visual effects (`initializeTypingEffect`)

2. **Configuration Management**: Centralized config object at top of `script.js`:
   ```javascript
   const CONFIG = {
       DISCORD_USER_ID: '1013495966998990950',
       SPOTIFY_CLIENT_ID: '316vzm4skw2oqoqmb42fj7irlxpq',
       UPDATE_INTERVAL: 30000,
       SPOTIFY_UPDATE_INTERVAL: 5000
   };
   ```

3. **Real-time Data Integration**: 
   - Uses Lanyard API for Discord status via both REST API and WebSocket
   - Implements fallback mechanisms and error handling
   - Real-time Spotify progress tracking with client-side calculations

4. **Responsive Widget System**: Two main widget areas:
   - **Discord Widget**: Shows avatar, username, status, and activity
   - **Spotify Widget**: Displays currently playing song with progress bar

### External Dependencies

**APIs:**
- **Lanyard API** (`https://api.lanyard.rest`): Provides Discord presence data and Spotify listening activity
- **Discord CDN**: For user avatars and assets
- **Spotify**: Album artwork and track metadata (via Lanyard)

**External Libraries:**
- Font Awesome 6.4.0 (icons)
- Google Fonts (Inter & JetBrains Mono)

## Development Guidelines

### Personalizing the Site

**Essential Changes for New Users:**
1. Update `CONFIG.DISCORD_USER_ID` in `script.js` with your Discord user ID
2. Modify personal information in `index.html`:
   - Profile name, bio text, social links
   - Social media URLs in `data-link` attributes
3. Replace `junkie.mp3` with your preferred background music
4. Update CSS color scheme in `:root` variables if desired

### API Integration Patterns

**Lanyard API Usage:**
- Primary endpoint: `GET https://api.lanyard.rest/v1/users/{USER_ID}`
- WebSocket endpoint: `wss://api.lanyard.rest/socket`
- The code handles both REST polling and WebSocket real-time updates
- Implements automatic reconnection and error recovery

**Status Update Pattern:**
```javascript
// Pattern used throughout for safe DOM updates
if (element && data) {
    element.textContent = data.value || fallbackValue;
}
```

### Visual Effects System

**Custom Cursor Implementation:**
- Smooth follow cursor with easing animation
- State changes on hover/click interactions  
- Controlled via `initializeCursor()` and CSS classes

**Typing Effect:**
- Cycles through multiple bio texts
- Configurable typing speed and pause durations
- Located in `initializeTypingEffect()`

**Background Animations:**
- CSS-only star field animation
- Ambient lighting effects with keyframe animations
- Particle system for visual depth

### Responsive Design

**Breakpoints:**
- Desktop: Default layout
- Tablet (≤1200px): Stacked widget layout
- Mobile (≤768px): Single column, adjusted typography
- Small mobile (≤480px): Compact spacing and hidden particles

**Layout Strategy:**
- Flexbox-based responsive grid system
- Widgets adapt from side-by-side to stacked
- Profile section remains centered at all screen sizes

### Performance Considerations

**API Call Management:**
- Discord status: 30-second polling + WebSocket real-time updates
- Spotify progress: 1-second client-side progress bar updates
- Spotify data: 5-second API polling
- Automatic error recovery with exponential backoff

**Asset Optimization:**
- External fonts are preloaded
- Images are lazy-loaded where possible
- CSS animations use `transform` and `opacity` for hardware acceleration

## Customization Points

### Theming
All colors are defined as CSS custom properties in `:root`. Key variables:
- `--bg-primary`: Main background color
- `--text-primary`: Primary text color  
- `--discord-*`: Discord status indicator colors
- `--spotify-green`: Spotify branding color

### Content Updates
- Bio texts: Update `texts` array in `initializeTypingEffect()`
- Social links: Modify HTML `data-link` attributes and add/remove grid items
- Status messages: Update `statusTexts` object in `updateDiscordUI()`

### Feature Extensions
- Additional widgets: Follow the widget HTML structure and add corresponding JavaScript updates
- New animations: Add CSS keyframes and trigger classes
- Extra API integrations: Follow the Lanyard integration pattern with error handling