#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

// Estructura para representar un punto en el plano
struct Point {
    int x, y;
};

// Función para encontrar el punto más abajo y más a la izquierda
int findBottomLeft(const vector<Point>& points) {
    int bottomLeft = 0;
    for (int i = 1; i < points.size(); ++i) {
        if (points[i].y < points[bottomLeft].y ||
            (points[i].y == points[bottomLeft].y && points[i].x < points[bottomLeft].x)) {
            bottomLeft = i;
        }
    }
    return bottomLeft;
}

// Función para calcular la orientación de tres puntos
int orientation(const Point& p, const Point& q, const Point& r) {
    int val = (q.y - p.y) * (r.x - q.x) -
              (q.x - p.x) * (r.y - q.y);

    if (val == 0) return 0;  // colineales
    return (val > 0) ? 1 : 2; // en sentido horario o antihorario
}

// Función comparadora para ordenar los puntos por ángulo respecto al punto de referencia
bool compare(const Point& p1, const Point& p2) {
    int o = orientation(referencePoint, p1, p2);
    if (o == 0)
        return ((p1.x - referencePoint.x) * (p1.x - referencePoint.x) +
                (p1.y - referencePoint.y) * (p1.y - referencePoint.y)) <
               ((p2.x - referencePoint.x) * (p2.x - referencePoint.x) +
                (p2.y - referencePoint.y) * (p2.y - referencePoint.y));
    return (o == 2);
}

// Función para encontrar la envolvente convexa utilizando el algoritmo Graham Scan
vector<int> convexHull(const vector<Point>& points) {
    vector<int> convexHullIndices;

    // Encontrar el punto más abajo y a la izquierda como punto de referencia
    int bottomLeft = findBottomLeft(points);
    referencePoint = points[bottomLeft];

    // Ordenar los puntos por ángulo respecto al punto de referencia
    vector<Point> sortedPoints(points);
    sort(sortedPoints.begin(), sortedPoints.end(), compare);

    // Iniciar el algoritmo Graham Scan
    stack<int> s;
    s.push(0);
    s.push(1);
    int i = 2;
    while (i < sortedPoints.size()) {
        while (s.size() >= 2) {
            int p1 = s.top();
            s.pop();
            int p2 = s.top();
            if (orientation(sortedPoints[p2], sortedPoints[p1], sortedPoints[i]) == 2) {
                s.push(p1);
                break;
            }
        }
        s.push(i++);
    }

    // Extraer los índices de los puntos en la envolvente convexa
    while (!s.empty()) {
        convexHullIndices.push_back(s.top());
        s.pop();
    }

    return convexHullIndices;
}

int main() {
    // Ejemplo de uso
    vector<Point> points = {{7, 6}, {8, 4}, {7, 2}, {3, 2}, {1, 6}, {1, 8}, {4, 9};
    vector<int> convexHullIndices = convexHull(points);

    // Imprimir los índices de la envolvente convexa
    for (int idx : convexHullIndices) {
        cout << idx << " ";
    }
    cout << endl;

    return 0;
}

