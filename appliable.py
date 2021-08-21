from sensors import *

class BinaryMatch:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class BinaryUnit:
    def __init__(self, u_radius, sensor_field_radius, etalon, event_diameter, dx,dy):
        self.u_radius = u_radius
        self.sensor_field_radius = sensor_field_radius
        self.A_min = etalon - event_diameter/2
        self.A_max = self.A_min + event_diameter
        self.dx = dx
        self.dy = dy

    def apply(self, pic, x,y):
        matches = []
        expected_x = x + self.dx
        expected_y = y + self.dy
        for r in range(0, self.u_radius + 1):
            X, Y = get_coords_for_radius(expected_x, expected_y, r)
            for i in range(len(X)):
                mean = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
                if mean >= self.A_min and mean <= self.A_max:
                    matches.append(BinaryMatch(X[i], Y[i]))
        return matches


class BinaryChainUnit:
    def __init__(self, binary_appliables):
        self.appliables = binary_appliables

    def apply(self, pic, x, y):
        matches = self.appliables[0].apply(pic, x, y)
        if len(matches) == 0:
            return []
        sprouts = [[match] for match in matches]

        done_sprouts = []
        chein_len = len(self.appliables)
        while True:
            if len(sprouts) == 0:
                break

            best_sprout = sprouts[0]
            if len(best_sprout) == chein_len:
                done_sprouts.append(list(sprouts[0]))
                sprouts.pop(0)
                continue

            # делаем проростки из вершины лучшего ростка
            top_note = best_sprout[-1]
            matches = self.appliables[len(best_sprout)].apply(top_note.x, top_note.y, pic)
            if len(matches) == 0:
                # лучший росток пришел в тупик, удяляем из рассмотрения
                sprouts.pop(0)
            else:
                # удаляем лучший росток, и заменяем его на н штук новых сортированных лучших ростков
                # "на единицу" выше старого лучшего
                new_best_sprouts = []
                for match in matches:
                    new_sprout = list(sprouts[0]).append(match)
                    new_best_sprouts.append(new_sprout)

                sprouts.pop(0)
                sprouts = new_best_sprouts + sprouts

        initial_matches = [sprout[0] for sprout in done_sprouts]
        return initial_matches

class NonBinaryMatch:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value = value

class NonBinaryUnit:
    def __init__(self, u_radius, sensor_field_radius, etalon, dx, dy):
        self.u_radius = u_radius
        self.sensor_field_radius = sensor_field_radius
        self.etalon = etalon
        self.dx = dx
        self.dy = dy

    def apply(self, pic, x, y): # returns float number
        X, Y = get_coords_less_or_eq_raduis(x + self.dx, y + self.dy, self.u_radius)
        nearest_mean = make_measurement(pic, X[0], Y[0], self.sensor_field_radius)
        for i in range(1, len(X)):
            mean = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
            if abs(mean - self.etalon) < abs(nearest_mean - self.etalon):
                nearest_mean = mean
        best_match = NonBinaryMatch(X[i], Y[i], nearest_mean)
        return best_match



