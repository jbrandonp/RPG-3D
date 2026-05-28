use bevy::prelude::*;

pub struct UiPlugin;

impl Plugin for UiPlugin {
    fn build(&self, app: &mut App) {
        app.add_systems(Startup, setup_hud);
    }
}

fn setup_hud(mut commands: Commands, _asset_server: Res<AssetServer>) {
    commands
        .spawn(NodeBundle {
            style: Style {
                width: Val::Percent(100.0),
                height: Val::Percent(100.0),
                justify_content: JustifyContent::SpaceBetween,
                ..default()
            },
            ..default()
        })
        .with_children(|parent| {
            parent
                .spawn(NodeBundle {
                    style: Style {
                        flex_direction: FlexDirection::Column,
                        align_items: AlignItems::FlexStart,
                        padding: UiRect::all(Val::Px(10.0)),
                        ..default()
                    },
                    ..default()
                })
                .with_children(|left_col| {
                    left_col.spawn(NodeBundle {
                        style: Style {
                            width: Val::Px(200.0),
                            height: Val::Px(20.0),
                            margin: UiRect::bottom(Val::Px(5.0)),
                            ..default()
                        },
                        background_color: Color::rgb(0.8, 0.1, 0.1).into(),
                        ..default()
                    });
                    left_col.spawn(NodeBundle {
                        style: Style {
                            width: Val::Px(150.0),
                            height: Val::Px(15.0),
                            margin: UiRect::bottom(Val::Px(5.0)),
                            ..default()
                        },
                        background_color: Color::rgb(0.1, 0.1, 0.8).into(),
                        ..default()
                    });
                    left_col.spawn(NodeBundle {
                        style: Style {
                            width: Val::Px(120.0),
                            height: Val::Px(10.0),
                            ..default()
                        },
                        background_color: Color::rgb(0.1, 0.8, 0.1).into(),
                        ..default()
                    });
                });

            parent
                .spawn(NodeBundle {
                    style: Style {
                        flex_direction: FlexDirection::Column,
                        align_items: AlignItems::FlexEnd,
                        padding: UiRect::all(Val::Px(10.0)),
                        ..default()
                    },
                    ..default()
                })
                .with_children(|right_col| {
                    right_col.spawn(NodeBundle {
                        style: Style {
                            width: Val::Px(150.0),
                            height: Val::Px(150.0),
                            ..default()
                        },
                        background_color: Color::rgba(0.2, 0.2, 0.2, 0.8).into(),
                        ..default()
                    });
                });
        });

    commands
        .spawn(NodeBundle {
            style: Style {
                width: Val::Percent(100.0),
                height: Val::Percent(100.0),
                position_type: PositionType::Absolute,
                justify_content: JustifyContent::Center,
                align_items: AlignItems::FlexEnd,
                padding: UiRect::bottom(Val::Px(20.0)),
                ..default()
            },
            ..default()
        })
        .with_children(|parent| {
            parent
                .spawn(NodeBundle {
                    style: Style {
                        width: Val::Px(400.0),
                        height: Val::Px(60.0),
                        border: UiRect::all(Val::Px(2.0)),
                        justify_content: JustifyContent::SpaceAround,
                        align_items: AlignItems::Center,
                        ..default()
                    },
                    background_color: Color::rgba(0.1, 0.1, 0.1, 0.9).into(),
                    border_color: Color::rgb(0.4, 0.4, 0.4).into(),
                    ..default()
                })
                .with_children(|action_bar| {
                    for _ in 0..5 {
                        action_bar.spawn(NodeBundle {
                            style: Style {
                                width: Val::Px(50.0),
                                height: Val::Px(50.0),
                                ..default()
                            },
                            background_color: Color::rgb(0.2, 0.2, 0.2).into(),
                            ..default()
                        });
                    }
                });
        });
}
