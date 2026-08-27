# ADD PROGRESS BAR (universal)
import time
import threading
import uuid
from datetime import datetime
from IPython.display import display, HTML, clear_output
from IPython.core.interactiveshell import InteractiveShell

# Get the shell instance
shell = InteractiveShell.instance()

# ════════════════════════════════════════════════════════════
# 1. CLEANUP (Prevent duplicate timers if you run this twice)
# ════════════════════════════════════════════════════════════
for event_type in ['pre_run_cell', 'post_run_cell']:
    if event_type in shell.events.callbacks:
        current_callbacks = shell.events.callbacks[event_type][:]
        for callback in current_callbacks:
            if 'timer' in callback.__name__ or 'progress' in callback.__name__:
                shell.events.unregister(event_type, callback)

# ════════════════════════════════════════════════════════════
# 2. GLOBAL STATE
# ════════════════════════════════════════════════════════════
_timer_running = False
_start_timestamp = 0
_display_id = None
_thread = None

# CSS for the animated bar (Indeterminate/Loading style)
# CHANGED: Replaced specific gray color with 'inherit' + opacity 
# to support both Dark and Light themes automatically.
_PROGRESS_CSS = """
<style>
@keyframes gradient-animation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.live-timer-bar {
    height: 4px;
    width: 100%;
    background: linear-gradient(270deg, #4caf50, #8bc34a, #cddc39);
    background-size: 200% 200%;
    animation: gradient-animation 2s ease infinite;
    border-radius: 2px;
    margin-bottom: 5px;
}
.live-timer-text {
    font-family: monospace;
    font-size: 12px;
    color: inherit;     /* Adapts to theme (Black or White) */
    opacity: 0.8;       /* Makes it slightly dimmed like original #666 */
}
</style>
"""

# ════════════════════════════════════════════════════════════
# 3. BACKGROUND THREAD FUNCTION
# ════════════════════════════════════════════════════════════
def update_progress_bar(display_id, start_time):
    """Updates the display handle every 0.1s while code runs."""
    while _timer_running:
        elapsed = time.time() - start_time
        
        # Create HTML content: CSS Bar + Text Timer
        html_content = f"""
        {_PROGRESS_CSS}
        <div class="live-timer-text">
            <div class="live-timer-bar"></div>
            Running... ⏱️ {elapsed:.1f}s
        </div>
        """
        
        # Update the specific output area
        try:
            display(HTML(html_content), display_id=display_id, update=True)
        except:
            break
            
        time.sleep(0.1)

# ════════════════════════════════════════════════════════════
# 4. HOOKS
# ════════════════════════════════════════════════════════════

def start_progress_hook(*args):
    global _timer_running, _start_timestamp, _display_id, _thread
    
    _timer_running = True
    _start_timestamp = time.time()
    
    # Generate a unique ID for this cell's output
    _display_id = str(uuid.uuid4())
    
    # Create the initial display object
    display(HTML(f"{_PROGRESS_CSS}<div class='live-timer-text'>Starting...</div>"), display_id=_display_id)
    
    # Start the background thread
    _thread = threading.Thread(target=update_progress_bar, args=(_display_id, _start_timestamp))
    _thread.daemon = True # Ensure thread dies if notebook crashes
    _thread.start()

def stop_progress_hook(*args):
    global _timer_running
    
    # Stop the thread loop
    _timer_running = False
    
    # Calculate final stats
    end_time = time.time()
    elapsed = end_time - _start_timestamp
    now_str = datetime.now().strftime("%I:%M:%S")
    
    # Wait briefly for thread to finish (optional)
    if _thread:
        _thread.join(timeout=0.2)
    
    # CHANGED: 
    # 1. color: inherit (Adapts to dark/light text)
    # 2. border-top: rgba(127,127,127,0.3) (Adapts border to look good on both backgrounds)
    final_html = f"""
    <div style="font-family: monospace; font-size: 12px; color: inherit; border-top: 1px solid rgba(127, 127, 127, 0.3); margin-top: 5px; padding-top: 2px;">
        ✅ {now_str}  (⏱️ {elapsed:.2f}s)
    </div>
    """
    
    # Update the display one last time
    try:
        display(HTML(final_html), display_id=_display_id, update=True)
    except:
        pass

# ════════════════════════════════════════════════════════════
# 5. REGISTER
# ════════════════════════════════════════════════════════════
shell.events.register('pre_run_cell', start_progress_hook)
shell.events.register('post_run_cell', stop_progress_hook)

print("✅ Live Progress Bar & Timer Enabled!")    height: 4px;
    width: 100%;
    background: linear-gradient(270deg, #4caf50, #8bc34a, #cddc39);
    background-size: 200% 200%;
    animation: gradient-animation 2s ease infinite;
    border-radius: 2px;
    margin-bottom: 5px;
}
.live-timer-text {
    font-family: monospace;
    font-size: 12px;
    color: inherit;     /* Adapts to theme (Black or White) */
    opacity: 0.8;       /* Makes it slightly dimmed like original #666 */
}
</style>
"""

# ════════════════════════════════════════════════════════════
# 3. BACKGROUND THREAD FUNCTION
# ════════════════════════════════════════════════════════════
def update_progress_bar(display_id, start_time):
    """Updates the display handle every 0.1s while code runs."""
    while _timer_running:
        elapsed = time.time() - start_time
        
        # Create HTML content: CSS Bar + Text Timer
        html_content = f"""
        {_PROGRESS_CSS}
        <div class="live-timer-text">
            <div class="live-timer-bar"></div>
            Running... ⏱️ {elapsed:.1f}s
        </div>
        """
        
        # Update the specific output area
        try:
            display(HTML(html_content), display_id=display_id, update=True)
        except:
            break
            
        time.sleep(0.1)

# ════════════════════════════════════════════════════════════
# 4. HOOKS
# ════════════════════════════════════════════════════════════

def start_progress_hook(*args):
    global _timer_running, _start_timestamp, _display_id, _thread
    
    _timer_running = True
    _start_timestamp = time.time()
    
    # Generate a unique ID for this cell's output
    _display_id = str(uuid.uuid4())
    
    # Create the initial display object
    display(HTML(f"{_PROGRESS_CSS}<div class='live-timer-text'>Starting...</div>"), display_id=_display_id)
    
    # Start the background thread
    _thread = threading.Thread(target=update_progress_bar, args=(_display_id, _start_timestamp))
    _thread.daemon = True # Ensure thread dies if notebook crashes
    _thread.start()

def stop_progress_hook(*args):
    global _timer_running
    
    # Stop the thread loop
    _timer_running = False
    
    # Calculate final stats
    end_time = time.time()
    elapsed = end_time - _start_timestamp
    now_str = datetime.now().strftime("%I:%M:%S")
    
    # Wait briefly for thread to finish (optional)
    if _thread:
        _thread.join(timeout=0.2)
    
    # CHANGED: 
    # 1. color: inherit (Adapts to dark/light text)
    # 2. border-top: rgba(127,127,127,0.3) (Adapts border to look good on both backgrounds)
    final_html = f"""
    <div style="font-family: monospace; font-size: 12px; color: inherit; border-top: 1px solid rgba(127, 127, 127, 0.3); margin-top: 5px; padding-top: 2px;">
        ✅ {now_str}  (⏱️ {elapsed:.2f}s)
    </div>
    """
    
    # Update the display one last time
    try:
        display(HTML(final_html), display_id=_display_id, update=True)
    except:
        pass

# ════════════════════════════════════════════════════════════
# 5. REGISTER
# ════════════════════════════════════════════════════════════
shell.events.register('pre_run_cell', start_progress_hook)
shell.events.register('post_run_cell', stop_progress_hook)

print("✅ Live Progress Bar & Timer Enabled!")
