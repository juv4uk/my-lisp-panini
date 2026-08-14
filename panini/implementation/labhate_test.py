import sys
import os

# Add current dir to path to import inference_engine_v0
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from inference_engine_v0 import Node, GraphState, Sutra, InferenceEngine

def print_graph(node: Node, indent: int = 0):
    props = ", ".join(f"{k}={v}" for k, v in node.properties.items())
    print("  " * indent + f"[{node.node_type}] {props}")
    for child in node.children:
        print_graph(child, indent + 1)

def main():
    engine = InferenceEngine()

    # Sūtra 3.2.123 "vartamāne laṭ"
    def match_lat(root: Node) -> bool:
        # Matches if situation has tense=vartamane and we haven't processed it yet
        tense = root.find_node('tense')
        has_lakara = root.find_node('lakara')
        has_tin = root.find_node('pratyaya')
        return tense is not None and tense.properties.get('value') == 'vartamane' and not has_lakara and not has_tin

    def apply_lat(root: Node):
        action = root.find_node('action')
        if action:
            action.children.append(Node('lakara', {'value': 'la~w'}))

    engine.register_sutra(Sutra(
        id="3.2.123", text="vartamāne laṭ", context=[],
        match_fn=match_lat, apply_fn=apply_lat
    ))

    # Sūtra 3.4.78 "tiptasjhi..." (lakara -> tin)
    def match_tin(root: Node) -> bool:
        return root.find_node('lakara') is not None and root.find_node('pratyaya') is None

    def apply_tin(root: Node):
        action = root.find_node('action')
        lakara = root.find_node('lakara')
        if action and lakara:
            action.children.remove(lakara)
            # Hardcoding 'ta' resolution for atmanepada kartr for this prototype
            action.children.append(Node('pratyaya', {'value': 'ta', 'type': 'tin', 'padam': 'atmanepadam'}))
            dhatu = action.find_node('dhatu')
            if dhatu:
                # Wrap dhatu in anga
                anga = Node('anga', {})
                action.children.remove(dhatu)
                anga.children.append(dhatu)
                action.children.append(anga)

    engine.register_sutra(Sutra(
        id="3.4.78", text="tiptasjhi...", context=[],
        match_fn=match_tin, apply_fn=apply_tin
    ))

    # Sūtra 3.1.68 "kartari śap"
    def match_sap(root: Node) -> bool:
        prat = root.find_node('pratyaya')
        anga = root.find_node('anga')
        vik = root.find_node('vikarana')
        return prat is not None and anga is not None and vik is None

    def apply_sap(root: Node):
        anga = root.find_node('anga')
        if anga:
            anga.children.append(Node('vikarana', {'value': 'Sa~p'}))

    engine.register_sutra(Sutra(
        id="3.1.68", text="kartari śap", context=['sarvadhatuke', 'dhatoh'],
        match_fn=match_sap, apply_fn=apply_sap
    ))

    # Sūtra 1.3.9 "tasya lopaḥ" (remove it-markers)
    def match_lopa(root: Node) -> bool:
        vik = root.find_node('vikarana')
        dhatu = root.find_node('dhatu')
        return (vik and '~' in vik.properties.get('value', '')) or (dhatu and '\\' in dhatu.properties.get('raw', ''))

    def apply_lopa(root: Node):
        vik = root.find_node('vikarana')
        if vik: vik.properties['value'] = 'a' # Sa~p -> a
        dhatu = root.find_node('dhatu')
        if dhatu:
            dhatu.properties['raw'] = dhatu.properties['clean']

    engine.register_sutra(Sutra(
        id="1.3.9", text="tasya lopaḥ", context=[],
        match_fn=match_lopa, apply_fn=apply_lopa
    ))

    # Sūtra 3.4.79 "ṭita ātmanepadānāṃ ṭere"
    def match_tere(root: Node) -> bool:
        prat = root.find_node('pratyaya')
        # match if pratyaya is 'ta'
        return prat is not None and prat.properties.get('value') == 'ta' and not root.find_node('vikarana') and not root.find_node('dhatu') # Wait, ensure lopa ran first
        
    def match_tere_correct(root: Node) -> bool:
        prat = root.find_node('pratyaya')
        lopa_ran = 'tasya lopaḥ' in str(root) # hack for prototype to force order
        # Actually, let's just check if it's 'ta' and lopa has been applied (vikarana is 'a')
        vik = root.find_node('vikarana')
        return prat is not None and prat.properties.get('value') == 'ta' and (vik and vik.properties.get('value') == 'a')

    def apply_tere(root: Node):
        prat = root.find_node('pratyaya')
        if prat:
            prat.properties['value'] = 'te'

    engine.register_sutra(Sutra(
        id="3.4.79", text="ṭita ātmanepadānāṃ ṭere", context=[],
        match_fn=match_tere_correct, apply_fn=apply_tere
    ))

    # INITIAL STATE
    dhatu_node = Node('dhatu', {'raw': 'qu-la\\B-a~z', 'clean': 'laB'})
    kartr_node = Node('karaka', {'semantic-role': 'agent', 'person': 3, 'number': 'eka'})
    action_node = Node('action', {}, [dhatu_node])
    roles_node = Node('roles', {}, [kartr_node])
    tense_node = Node('tense', {'value': 'vartamane'})
    situation_node = Node('situation', {}, [action_node, tense_node, roles_node])

    initial_state = GraphState(id="state-0", root=situation_node)

    print("=== INITIAL STATE (vivakṣā) ===")
    print_graph(initial_state.root)
    print()

    # DERIVE
    final_state = engine.derive(initial_state)

    print("=== DERIVATION HISTORY ===")
    for h in final_state.history:
        print(f" -> {h}")
    print()

    print("=== FINAL STATE ===")
    print_graph(final_state.root)

if __name__ == "__main__":
    main()
