import random
demand, bounds, costs = 100.0, [[20.0, 90.0], [-20.0, 20.0]], [0.50, 0.15]
particles = [[random.uniform(b[0], b[1]) for b in bounds] for _ in range(20)]
velocities = [[0.0, 0.0] for _ in range(20)]
pbest = list(particles)
gbest = min(pbest, key=lambda p: sum(p*c for p, c in zip(p, costs)) + 1000 * (sum(p) - demand)**2)

for _ in range(50):
    for i, p in enumerate(particles):
        
        velocities[i] = [0.7 * v + 1.5 * random.random() * (pb - px) + 1.5 * random.random() * (gb - px) 
                         for v, pb, gb, px in zip(velocities[i], pbest[i], gbest, p)]
        particles[i] = [max(b[0], min(b[1], px + v)) for b, px, v in zip(bounds, p, velocities[i])]
        
        
        score = lambda x: sum(a*c for a, c in zip(x, costs)) + 1000 * (sum(x) - demand)**2
        if score(particles[i]) < score(pbest[i]):
            pbest[i] = list(particles[i])
            if score(particles[i]) < score(gbest):
                gbest = list(particles[i])

print(f"Optimal Schedule -> Generator: {gbest[0]:.2f} kW, Battery: {gbest[1]:.2f} kW")
print(f"Total Dispatched  -> {sum(gbest):.2f} kW (Target: {demand} kW)")
