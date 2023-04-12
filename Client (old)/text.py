import pygame
import pygame.freetype

def main():
    def resetScreen():
        if current_idx >= len(current):
            # if the sentence is complete, let's prepare the
            # next surface
            current_idx = 0
            current = next(data)
            text_surf_rect = font.get_rect(current)
            baseline = text_surf_rect.y
            text_surf = pygame.Surface(text_surf_rect.size)
            text_surf_rect.center = screen.get_rect().center
            metrics = font.get_metrics(current)
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # just some demo data for you to type
    data = "This is an example"
    current = data
    current_idx = 0 # points to the current letter, as you have already guessed
    
    font = pygame.freetype.Font(None, 50)
    font.origin = True
    font_height = font.get_sized_height()
    M_ADV_X = 4
    
    text_surf_rect = font.get_rect(current)
    baseline = text_surf_rect.y
    text_surf = pygame.Surface(text_surf_rect.size)
    text_surf_rect.center = screen.get_rect().center
    metrics = font.get_metrics(current)

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.unicode == current[current_idx].lower():
                    # if we press the correct letter, move the index
                    current_idx += 1
                    if current_idx > len(data):
                        resetScreen()

        # clear everything                        
        screen.fill('white')
        text_surf.fill('white')
        
        x = 0
        # render each letter of the current sentence one by one
        for (idx, (letter, metric)) in enumerate(zip(current, metrics)):
            # select the right color
            if idx == current_idx:
                color = 'lightblue'
            elif idx < current_idx:
                color = 'lightgrey'
            else:
                color = 'black'
            # render the single letter
            font.render_to(text_surf, (x, baseline), letter, color)
            # and move the start position
            x += metric[M_ADV_X]
          
        screen.blit(text_surf, text_surf_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
