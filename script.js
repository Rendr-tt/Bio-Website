const CONFIG = {
    DISCORD_USER_ID: '1013495966998990950',
    SPOTIFY_CLIENT_ID: '316vzm4skw2oqoqmb42fj7irlxpq',
    UPDATE_INTERVAL: 30000,
    SPOTIFY_UPDATE_INTERVAL: 5000
};

let currentDiscordHandle = 'rendr.tt';
let lastDiscordUpdate = 0;
let lastSpotifyUpdate = 0;
let spotifyProgress = 0;
let spotifyDuration = 0;
let spotifyCurrentTime = 0;
let progressInterval = null;
let backgroundMusic = false;
let hasEnteredSite = false;
let isMuted = false;
let currentSpotifyData = null;



function copyDiscordUsername() {
    const username = 'rendr.tt';
    navigator.clipboard.writeText(username).then(() => {
        const usernameEl = document.getElementById('discord-username');
        const originalText = usernameEl.textContent;
        usernameEl.textContent = 'Copied!';
        setTimeout(() => {
            usernameEl.textContent = originalText;
        }, 1000);
    });
}



function initializeCursor() {
    const cursor = document.querySelector('.cursor');
    const cursorDot = document.querySelector('.cursor-dot');
    const cursorRing = document.querySelector('.cursor-ring');
    
    if (!cursor) return;
    
    let mouseX = 0;
    let mouseY = 0;
    let cursorX = 0;
    let cursorY = 0;
    
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });
    
    function updateCursor() {
        cursorX += (mouseX - cursorX) * 0.15;
        cursorY += (mouseY - cursorY) * 0.15;
        
        cursor.style.transform = `translate(${cursorX}px, ${cursorY}px)`;
        requestAnimationFrame(updateCursor);
    }
    updateCursor();
    
    const interactiveElements = document.querySelectorAll('a, .avatar, .main-avatar-img, .album-art, .social-link, .entry-text, .audio-control');
    
    interactiveElements.forEach(element => {
        element.addEventListener('mouseenter', () => {
            cursor.classList.add('hover');
        });
        
        element.addEventListener('mouseleave', () => {
            cursor.classList.remove('hover');
        });
    });
}

function initializeEntryPage() {
    const entryPage = document.getElementById('entry-page');
    const entryButton = document.getElementById('entry-button');
    const mainSite = document.getElementById('main-site');
    const audioControl = document.getElementById('audio-control');
    const audioIcon = document.getElementById('audio-icon');
    
    backgroundMusic = document.getElementById('background-music');
    backgroundMusic.volume = 0.8; // Set volume to 80%
    
    audioControl.addEventListener('click', function(e) {
        e.stopPropagation();
        toggleAudio();
    });
    
    entryButton.addEventListener('click', function() {
        if (hasEnteredSite) return;
        hasEnteredSite = true;
        
        audioControl.classList.add('visible');
        
        if (backgroundMusic && !isMuted) {
            backgroundMusic.currentTime = 0;
            
            const playPromise = backgroundMusic.play();
            if (playPromise !== undefined) {
                playPromise.then(() => {
                    console.log('Musique démarrée avec succès');
                }).catch(error => {
                    console.log('Erreur lors du démarrage de la musique:', error);
                });
            }
            
            backgroundMusic.addEventListener('ended', function() {
                if (!isMuted) {
                    this.currentTime = 0;
                    this.play();
                }
            });
        }
        
        entryPage.classList.add('fade-out');
        
        setTimeout(() => {
            entryPage.style.display = 'none';
            mainSite.style.display = 'block';
            
            initializeMainSite();
        }, 800);
function initializeEntryPage() {
    const entryPage = document.getElementById('entry-page');
    const entryButton = document.getElementById('entry-button');
    const mainSite = document.getElementById('main-site');
    const audioControl = document.getElementById('audio-control');
    const audioIcon = document.getElementById('audio-icon');
    
    backgroundMusic = document.getElementById('background-music');
    backgroundMusic.volume = 0.8; // Set volume to 80%
    
    audioControl.addEventListener('click', function(e) {
        e.stopPropagation();
        toggleAudio();
    });
    
    entryButton.addEventListener('click', function() {
        if (hasEnteredSite) return;
        hasEnteredSite = true;
        
        audioControl.classList.add('visible');
        
        if (backgroundMusic && !isMuted) {
            backgroundMusic.currentTime = 0;
            
            const playPromise = backgroundMusic.play();
            if (playPromise !== undefined) {
                playPromise.then(() => {
                    console.log('Musique démarrée avec succès');
                }).catch(error => {
                    console.log('Erreur lors du démarrage de la musique:', error);
                });
            }
            
            backgroundMusic.addEventListener('ended', function() {
                if (!isMuted) {
                    this.currentTime = 0;
                    this.play();
                }
            });
        }
        
        entryPage.classList.add('fade-out');
        
        setTimeout(() => {
            entryPage.style.display = 'none';
            mainSite.style.display = 'block';
            
            initializeMainSite();
        }, 800);  
    });
    
    function toggleAudio() {
    if (backgroundMusic.paused) {
        backgroundMusic.muted = false;
        backgroundMusic.play().then(() => {
            console.log("Music resumed.");
            audioIcon.className = "fas fa-volume-up";
            audioControl.classList.remove("muted");
        }).catch(err => console.log("Error resuming:", err));
    } else {
        backgroundMusic.pause();
        backgroundMusic.muted = true;
        console.log("Music paused.");
        audioIcon.className = "fas fa-volume-mute";
        audioControl.classList.add("muted");
    }
    

}


}


function initializeMainSite() {
    initializeTypingEffect();
    initializeLastSeen();
    updateDiscordStatus();
    updateSpotifyStatus();
    
    setInterval(updateDiscordStatus, CONFIG.UPDATE_INTERVAL);
    setInterval(updateSpotifyStatus, CONFIG.SPOTIFY_UPDATE_INTERVAL);
    setInterval(updateLastSeen, 60000);
    
    setInterval(updateSpotifyProgress, 1000);
}

function initializeTypingEffect() {
    const typingText = document.querySelector('.typing-text');
    if (!typingText) return;
    
    const texts = [
        'me and windsurf against the world',
        'Prolly listening to music',
        'In love with python',
        'a chill guy'
    ];
    
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    
    function typeWriter() {
        const currentText = texts[textIndex];
        
        if (isDeleting) {
            typingText.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typingText.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
        }
        
        let typeSpeed = isDeleting ? 50 : 100;
        
        if (!isDeleting && charIndex === currentText.length) {
            typeSpeed = 2000;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % texts.length;
            typeSpeed = 500;
        }
        
        setTimeout(typeWriter, typeSpeed);
    }
    
    typeWriter();
}

function initializeLastSeen() {
    updateLastSeen();
}

function updateLastSeen() {
    const lastSeenElement = document.getElementById('last-seen');
    if (!lastSeenElement) return;
    
    const now = new Date();
    const timeString = now.toLocaleTimeString('fr-FR', {
        hour: '2-digit',
        minute: '2-digit'
    });
    
    lastSeenElement.textContent = `Last seen: ${timeString}`;
}

function connectWebSocket() {
    const socket = new WebSocket('wss://api.lanyard.rest/socket');
    
    socket.onopen = () => {
        socket.send(JSON.stringify({
            op: 2,
            d: {
                subscribe_to_id: CONFIG.DISCORD_USER_ID
            }
        }));
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        if (data.t === 'PRESENCE_UPDATE' && data.d) {
            updateDiscordUI(data.d);
        }
    };

    socket.onclose = () => {
        setTimeout(connectWebSocket, 1000);
    };
}

async function updateDiscordStatus() {
    try {
        // Initial fetch
        const response = await fetch(`https://api.lanyard.rest/v1/users/${CONFIG.DISCORD_USER_ID}`);
        const data = await response.json();
        
        if (data.success && data.data) {
            updateDiscordUI(data.data);
        }
        
        // Set up WebSocket for real-time updates
        connectWebSocket();
    } catch (error) {
        console.log('Error fetching Discord data:', error);
        setTimeout(updateDiscordStatus, 5000);
    }
}

function updateDiscordUI(userData) {
    const avatar = document.getElementById('discord-avatar');
    const username = document.getElementById('discord-username');
    const activity = document.getElementById('discord-activity');
    const statusDot = document.getElementById('discord-status-dot');
    const statusBadge = document.getElementById('discord-status');
    const mainAvatar = document.getElementById('main-avatar');
    const mainStatusDot = document.getElementById('main-status-dot');
    const mainStatusText = document.getElementById('main-status-text');
    
    if (avatar && (userData.discord_user || userData.user)) {
        const user = userData.discord_user || userData.user;
        const avatarUrl = user.avatar 
            ? `https://cdn.discordapp.com/avatars/${user.id}/${user.avatar}?size=128`
            : `https://cdn.discordapp.com/embed/avatars/0.png`;
        
        if (avatarUrl !== avatar.src) {
            avatar.src = avatarUrl;
            if (mainAvatar) mainAvatar.src = avatarUrl;
        }
    }
    
    if (username && (userData.discord_user || userData.user)) {
        const user = userData.discord_user || userData.user;
        username.textContent = user.global_name || user.username || 'rendr.tt';
    }
    
    const status = userData.discord_status || 'offline';
    if (statusDot) {
        statusDot.className = `status-indicator ${status}`;
    }
    if (statusBadge) {
        statusBadge.className = `status-badge ${status}`;
    }
    
    if (mainStatusDot) {
        mainStatusDot.className = `status-dot ${status}`;
    }
    
    const statusTexts = {
        'online': 'online - Im prolly gaming, if not, then im listening to music',
        'idle': 'Absent - but will respond later',
        'dnd': 'Do Not Disturb - please dont.',
        'offline': 'Offline - leave a message'
    };
    
    if (mainStatusText) {
        mainStatusText.textContent = statusTexts[status] || 'Statut inconnu';
    }
    
    if (activity) {
        const activityText = activity.querySelector('.activity-text');
        if (userData.activities && userData.activities.length > 0) {
            const customStatus = userData.activities.find(act => act.type === 4);
            if (customStatus) {
                const emoji = customStatus.emoji ? `${customStatus.emoji.name} ` : '';
                const state = customStatus.state || '';
                activityText.textContent = `${emoji}${state}`.trim() || 'Custom Status';
            } else {
                const currentActivity = userData.activities[0];
                if (currentActivity.type === 0) { 
                    activityText.textContent = `Playing ${currentActivity.name}`;
                } else if (currentActivity.type === 2) { 
                    activityText.textContent = `Listening to ${currentActivity.name}`;
                } else if (currentActivity.type === 3) { 
                    activityText.textContent = `Watching ${currentActivity.name}`;
                } else {
                    activityText.textContent = currentActivity.name;
                }
            }
        } else {
            const activityStatusTexts = {
                'online': 'Online',
                'idle': 'Away',
                'dnd': 'Do Not Disturb',
                'offline': 'Offline'
            };
            activityText.textContent = activityStatusTexts[status] || 'Offline';
        }
    }
}

async function updateSpotifyStatus() {
    try {
        const response = await fetch(`https://api.lanyard.rest/v1/users/${CONFIG.DISCORD_USER_ID}`);
        const data = await response.json();
        
        if (data.success && data.data && data.data.spotify) {
            updateSpotifyUI(data.data.spotify);
        } else {
            updateSpotifyUI(null);
        }
    } catch (error) {
        console.log('spotify error?:', error);
        updateSpotifyUI(null);
    }
}

function updateSpotifyProgress() {
    if (!currentSpotifyData) return;
    
    const progressFill = document.getElementById('spotify-progress');
    const currentTimeElement = document.getElementById('current-time');
    const totalTimeElement = document.getElementById('total-time');
    
    const progress = ((Date.now() - currentSpotifyData.timestamps.start) / (currentSpotifyData.timestamps.end - currentSpotifyData.timestamps.start)) * 100;
    const clampedProgress = Math.min(Math.max(progress, 0), 100);
    
    if (progressFill) {
        progressFill.style.width = `${clampedProgress}%`;
    }
    
    const currentMs = Date.now() - currentSpotifyData.timestamps.start;
    const totalMs = currentSpotifyData.timestamps.end - currentSpotifyData.timestamps.start;
    
    if (currentTimeElement) {
        currentTimeElement.textContent = formatTime(Math.max(0, currentMs));
    }
    if (totalTimeElement) {
        totalTimeElement.textContent = formatTime(totalMs);
    }
}

function updateSpotifyUI(spotifyData) {
    const trackElement = document.getElementById('spotify-track');
    const artistElement = document.getElementById('spotify-artist');
    const albumElement = document.getElementById('spotify-album');
    const albumContainer = document.querySelector('.album-container');
    const playingIndicator = document.getElementById('spotify-playing');
    const progressContainer = document.getElementById('spotify-progress-container');
    
    currentSpotifyData = spotifyData;
    
    if (spotifyData) {
        if (trackElement) trackElement.textContent = spotifyData.song;
        if (artistElement) artistElement.textContent = spotifyData.artist;
        if (albumElement) {
            albumElement.src = spotifyData.album_art_url;
            albumElement.classList.add('visible');
        }
        if (albumContainer) {
            albumContainer.classList.remove('hidden');
        }
        
        if (playingIndicator) {
            playingIndicator.classList.add('playing');
        }
        
        if (progressContainer) {
            progressContainer.classList.add('visible');
        }
        
        updateSpotifyProgress();
    } else {
        if (trackElement) trackElement.textContent = 'Not playing';
        if (artistElement) artistElement.textContent = '-';
        if (albumElement) {
            albumElement.src = '';
            albumElement.classList.remove('visible'); 
        }
        if (albumContainer) {
            albumContainer.classList.add('hidden');
        }
        if (playingIndicator) {
            playingIndicator.classList.remove('playing');
        }
        if (progressContainer) {
            progressContainer.classList.remove('visible');
        }
    }
}

function formatTime(ms) {
    const seconds = Math.floor(ms / 1000);
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
}

function showNotification(title, message, type = 'success', duration = 3000) {
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notif => notif.remove());
    
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    
    const icon = type === 'success' ? 'fas fa-check-circle' : 'fas fa-exclamation-circle';
    
    notification.innerHTML = `
        <div class="notification-icon">
            <i class="${icon}"></i>
        </div>
        <div class="notification-content">
            <div class="notification-title">${title}</div>
            <div class="notification-message">${message}</div>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 300);
    }, duration);
}

async function copyToClipboard(text) {
    try {
        if (navigator.clipboard && window.isSecureContext) {
            await navigator.clipboard.writeText(text);
            return true;
        } else {
            const textArea = document.createElement('textarea');
            textArea.value = text;
            textArea.style.position = 'fixed';
            textArea.style.left = '-999999px';
            textArea.style.top = '-999999px';
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();
            
            const result = document.execCommand('copy');
            textArea.remove();
            return result;
        }
    } catch (err) {
        console.error('error beim kopieren:', err);
        return false;
    }
}

function initializeSocialLinks() {
    const socialLinks = document.querySelectorAll('.social-link');
    
    socialLinks.forEach(link => {
        link.addEventListener('click', async (e) => {
            e.preventDefault();
            
            const linkUrl = link.getAttribute('data-link');
            const platform = link.getAttribute('data-platform');
            
            if (!linkUrl) {
                showNotification(
                    'Erreur',
                    'error',
                    'error'
                );
                return;
            }
            
            link.classList.add('copying');
            setTimeout(() => {
                link.classList.remove('copying');
            }, 150);
            
            const success = await copyToClipboard(linkUrl);
            
            if (success) {
                showNotification(
                    `${platform} coppied !`,
                    `coppied`,
                    'success'
                );
            } else {
                showNotification(
                    'error trying to copy!',
                    'error???',
                    'error'
                );
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    initializeCursor();
    initializeEntryPage();
    initializeSocialLinks();
});