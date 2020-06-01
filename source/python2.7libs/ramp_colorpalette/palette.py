"""Color Palette Ramp

Use K-Means clustering algorithm in VEX to set a ramp based on an
image's color palette.

All of these functions live on the HDA in the Scripts section.
"""
import hou


def set_ramp(node, event_type, **kwargs):
    """Set the ramp when a certain parameter changes.

    :param node: This node
    :type node: :class:`hou.Node`
    :param event_type: Houdini Node Event
    :type event_type: :class:`hou.nodeEventType`
    :param kwargs: Any extra keyword arugments passed by the event
    :type kwargs: dict
    """

    if not event_type == hou.nodeEventType.ParmTupleChanged:
        return

    parm_changed = kwargs.get("parm_tuple")
    if not parm_changed:
        return

    if parm_changed.name() not in callback_parm_names(node):
        return

    ramp_parm = node.parm("ramp")
    stops = node.evalParm("stops")
    interpolation = hou.rampBasis.Linear

    try:
        colors = node.node(
            "RGB_COLORS"
        ).geometry().floatListAttribValue("colors")
    except AttributeError:
        return
    except hou.OperationFailed:
        return

    colors = [colors[i:i + 3] for i in range(0, len(colors), 3)]
    keys = [x * (1.0 / (stops - 1)) for x in range(stops)]
    basis = (interpolation, interpolation)
    ramp = hou.Ramp(basis, keys, colors)
    ramp_parm.set(ramp)


def callback_parm_names(node):
    """Find all parameter names in the `Image` folder.

    Each parameter will be used to run :meth:`set_ramp` function.

    :param node: This node
    :type node: :class:`hou.Node`
    :return: List of parameter names in the `Image` folder
    :rtype: list
    """
    ptg = node.parmTemplateGroup()
    folder = ptg.findFolder("Image")
    parm_names = recurse_parm_template(folder, list())
    return parm_names


def recurse_parm_template(template, parm_names):
    """Gather parm names recursively from a Houdini folder parm.

    :param template: Houdini parm template/folder to gather names from
    :type template: :class:`hou.FolderParmTemplate`
    :param parm_names: List of parameter names
    :type parm_names: list
    :return: List of parameter names in the folder
    :rtype: list
    """
    if not isinstance(template, hou.FolderParmTemplate):
        return parm_names.append(template.name())
    for parm_template in template.parmTemplates():
        if not isinstance(parm_template, hou.FolderParmTemplate):
            parm_names.append(parm_template.name())
        else:
            parm_names = recurse_parm_template(parm_template, parm_names)
    return parm_names


def set_seed(node):
    """Initialize random cluster seed parameter.

    :param node: This node
    :type node: :class:`hou.Node`
    """
    seed = 341 * node.sessionId() + 92
    node.parm("seed").set(seed % 10000)


def add_callback(node):
    """Add NodeEventCallBack when certain parms are changed.

    :param node: This node
    :type node: :class:`hou.Node`
    """
    node.addEventCallback((hou.nodeEventType.ParmTupleChanged, ), set_ramp)


def auto_output(node):
    """Change the output type depending on the node's input.

    :param node: This node
    :type node: :class:`hou.Node`
    """
    if not node.inputs():
        node.parm("output").set(2)
    else:
        node.parm("output").set(0)


def toggle_aces(node):
    """Automatically set checkbox for converting sRGB to AcesCG

    :param node: This node
    :type node: :class:`hou.Node`
    """
    enable_aces = False
    aces_parm = node.parmTuple("do_ACEScg")
    linearize_parm = node.parmTuple("linearize")
    try:
        active_displays = hou.Color.ocio_activeDisplays()
        if "ACES" in active_displays:
            aces_parm.set((1,))
            linearize_parm.disable(True)
            enable_aces = True
    except AttributeError:
        # Build < 18.0.460
        ocio_spaces = hou.Color.ocio_spaces()
        if "ACES - ACEScg" in ocio_spaces:
            # Don't disable it, but also don't assume ACES is active
            enable_aces = True
    if not enable_aces:
        aces_parm.disable(True)
