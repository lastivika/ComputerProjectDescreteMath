def read_graph_from_csv(filename, directed=False):
    try:
        from graph import Graph
    except ImportError:
        print("ПОМИЛКА: Не знайдено клас Graph!")
        return None
    
    graph = Graph(directed=directed)
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        if not lines:
            print("Увага: файл порожній!")
            return graph
        
        lines_read = 0
        edges_added = 0
        errors = 0
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            if not line:
                continue
            
            if line.startswith('#'):
                continue
            
            lines_read += 1
            parts = line.split(',')
            
            if len(parts) < 2:
                print(f"Рядок {line_num}: '{line}' - недостатньо даних")
                errors += 1
                continue
            
            from_vertex = parts[0].strip()
            to_vertex = parts[1].strip()
            
            if not from_vertex or not to_vertex:
                print(f"Рядок {line_num}: порожні назви вершин")
                errors += 1
                continue
            
            weight = 1
            
            if len(parts) >= 3:
                weight_str = parts[2].strip()
                if weight_str:
                    try:
                        weight = float(weight_str)
                    except ValueError:
                        print(f"Рядок {line_num}: вага '{weight_str}' не число, використовуємо 1")
                        weight = 1
            
            success = graph.add_edge(from_vertex, to_vertex, weight)
            if success:
                edges_added += 1
            else:
                errors += 1
        
        print(f"Файл успішно оброблено!")
        print(f"Прочитано рядків: {lines_read}")
        print(f"Додано ребер: {edges_added}")
        print(f"Вершин у графі: {graph.vertex_count}")
        print(f"Помилок: {errors}")
        
        return graph
        
    except FileNotFoundError:
        print(f"ПОМИЛКА: Файл '{filename}' не знайдено!")
        return None
    
    except Exception as e:
        print(f"ПОМИЛКА: {e}")
        return None

def create_sample_csv(filename="graph_data.csv"):
    sample_data = [
        "A,B,5",
        "A,C,3",
        "B,D,2",
        "C,D,1",
        "D,E,4",
        "E,F,2",
        "B,E,6",
        "F,A,7",
        "G,H,10",
        "H,I,8",
        "G,I,15"
    ]
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in sample_data:
                file.write(line + '\n')
        
        print(f"Створено приклад файлу: {filename}")
        return True
        
    except Exception as e:
        print(f"Помилка при створенні файлу: {e}")
        return False

def save_graph_to_csv(graph, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("# Граф збережено з програми\n")
            file.write("# from,to,weight\n")
            
            edges = graph.get_edges()
            
            for from_v, to_v, weight in edges:
                file.write(f"{from_v},{to_v},{weight}\n")
        
        print(f"Граф збережено у файл: {filename}")
        print(f"Збережено ребер: {len(edges)}")
        return True
        
    except Exception as e:
        print(f"Помилка при збереженні: {e}")
        return False