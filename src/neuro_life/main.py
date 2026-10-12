import pygame

pygame.init()

size_x = 800
size_y = 600

screen = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Neuro Life")

running = True

clock = pygame.time.Clock()

agent_x = 400
agent_y = 300
agent_radius = 10
vector_x = True
vector_y = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if agent_x <= agent_radius or agent_x >= size_x - agent_radius:
        vector_x = not vector_x
    if agent_y <= agent_radius or agent_y >= size_y - agent_radius:
        vector_x = not vector_y
    
    if vector_x:
            agent_x += 1
    else:
        agent_x -= 1

    if vector_y:
        agent_y += 1
    else:
        agent_y -= 1

        
    screen.fill((30, 30, 30))
    
    pygame.draw.circle(screen, (200, 200, 200), 
                       (agent_x, agent_y), 
                       agent_radius
    )
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
