import copy
import dataclasses
from typing import Any, Callable, Dict, List, Optional, Tuple

@dataclasses.dataclass
class Node:
    node_type: str
    properties: Dict[str, Any]
    children: List['Node'] = dataclasses.field(default_factory=list)

    def find_node(self, node_type: str) -> Optional['Node']:
        if self.node_type == node_type:
            return self
        for child in self.children:
            res = child.find_node(node_type)
            if res: return res
        return None

    def clone(self) -> 'Node':
        return Node(
            node_type=self.node_type,
            properties=copy.deepcopy(self.properties),
            children=[c.clone() for c in self.children]
        )

@dataclasses.dataclass
class GraphState:
    id: str
    root: Node
    history: List[str] = dataclasses.field(default_factory=list)

    def clone(self, new_id: str) -> 'GraphState':
        return GraphState(
            id=new_id,
            root=self.root.clone(),
            history=list(self.history)
        )

@dataclasses.dataclass
class Sutra:
    id: str
    text: str
    context: List[str]
    match_fn: Callable[[Node], bool]
    apply_fn: Callable[[Node], None]

class InferenceEngine:
    def __init__(self):
        self.sutras: List[Sutra] = []

    def register_sutra(self, sutra: Sutra):
        self.sutras.append(sutra)

    def step(self, state: GraphState) -> Optional[GraphState]:
        # 1. Match
        candidates = []
        for sutra in self.sutras:
            if sutra.match_fn(state.root):
                candidates.append(sutra)
        
        if not candidates:
            return None

        # 2. Conflict Resolution
        # In v0.1 we just pick the first applicable one to simulate basic execution
        # (A real engine would do apavada/vipratisedha here)
        winner = candidates[0]
        
        # 3. Rewrite
        new_state = state.clone(f"state-{len(state.history)+1}")
        winner.apply_fn(new_state.root)
        new_state.history.append(f"Applied {winner.id} '{winner.text}'")
        
        return new_state

    def derive(self, initial_state: GraphState, max_steps: int = 10) -> GraphState:
        current = initial_state
        for _ in range(max_steps):
            next_state = self.step(current)
            if not next_state:
                break
            current = next_state
        return current
